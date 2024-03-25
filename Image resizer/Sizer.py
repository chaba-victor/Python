from PIL import Image
import os
import re

# Parameters
INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
QUALITY = 85  # Adjust as needed

BREAKPOINTS = {
    "xs": 400,
    "sm": 640,
    "md": 768,
    "lg": 1024,
    "xl": 1280
}

# Helper function to replace multiple spaces with single hyphen
def name_sanitizer(name):
    name = re.sub(r'\s+', '-', name)
    return re.sub(r'-+', '-', name)

def resize_image(input_path, output_path, breakpoint, ext, has_alpha, width, height):
    max_width = BREAKPOINTS[breakpoint]
    
    # If the image's width is less than the breakpoint, skip it.
    if width <= max_width:
        return False
        
    aspect_ratio = height / width
    new_width = max_width
    new_height = int(aspect_ratio * max_width)
    img = Image.open(input_path)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    
    if output_path:  # Add this condition
        if has_alpha or ext == '.png':
            img.save(output_path.replace('.jpg', '.png'), 'PNG', quality=QUALITY)
            img.convert("RGB").save(output_path.replace('.png', '.webp'), 'WEBP', quality=QUALITY)
        else:
            img.save(output_path, 'JPEG', quality=QUALITY)
            img.save(output_path.replace('.jpg', '.webp'), 'WEBP', quality=QUALITY)

    
    img.close()
    return True


def main():
    total_savings = 0
    previous_bp = None  # Initialize previous_bp

    for image_name in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, image_name)
        
        if not os.path.isfile(input_path):
            continue
        
        ext = os.path.splitext(image_name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            continue
        
        sanitized_name = name_sanitizer(os.path.splitext(image_name)[0])
        
        output_folder = os.path.join(OUTPUT_DIR, sanitized_name)
        os.makedirs(output_folder, exist_ok=True)

        # Backup original
        backup_folder = os.path.join(output_folder, 'backup')
        os.makedirs(backup_folder, exist_ok=True)
        backup_image_path = os.path.join(backup_folder, f"{sanitized_name}_original{ext}")
        os.rename(input_path, backup_image_path)

        # Check for alpha/transparency in image
        img = Image.open(backup_image_path)
        width, height = img.size
        has_alpha = img.mode == 'RGBA' or 'A' in img.getbands()
        img.close()

        # Create picture tag txt
        picture_tags = []
        previous_bp_width = 0
        bps = list(BREAKPOINTS.items())

        for i, (bp, bp_width) in enumerate(bps):
            output_image_path = os.path.join(output_folder, f"{sanitized_name}_{bp}.jpg")

            if resize_image(backup_image_path, output_image_path, bp, ext, has_alpha, width, height):
                # Check if it's the last breakpoint the image will be resized to.
                is_last_bp = i == len(bps) - 1 or (i < len(bps) - 1 and not resize_image(backup_image_path, "", bps[i+1][0], ext, has_alpha, width, height))

                if is_last_bp:
                    media_query = f'(min-width: {previous_bp_width + 1}px)'
                else:
                    media_query = f'(max-width: {bp_width}px)'

                if has_alpha or ext == '.png':
                    picture_tags.append(
                        f'<source srcset="{sanitized_name}_{bp}.webp 1x, {sanitized_name}_{bp}.png 1x" media="{media_query}">')
                else:
                    picture_tags.append(
                        f'<source srcset="{sanitized_name}_{bp}.webp 1x, {sanitized_name}_{bp}.jpg 1x" media="{media_query}">')

                previous_bp_width = bp_width
                previous_bp = bp
            else:
                break



        # Add <img> tag only if previous_bp is not None
        if previous_bp:
            picture_tags.append(f'<img src="{sanitized_name}_{previous_bp}.jpg" alt="...">')

        # Write to txt file
        with open(os.path.join(output_folder, 'picture_tag.txt'), 'w') as txt_file:
            txt_file.write('<picture>\n')
            for tag in picture_tags:
                txt_file.write('    ' + tag + '\n')
            txt_file.write('</picture>')

        # Calculate savings
        total_savings += os.path.getsize(backup_image_path) - sum([os.path.getsize(os.path.join(output_folder, f"{sanitized_name}_{bp}.jpg")) for bp in BREAKPOINTS if os.path.exists(os.path.join(output_folder, f"{sanitized_name}_{bp}.jpg"))])

    print(f"Total savings: {total_savings / (1024 * 1024):.2f} MB")


if __name__ == '__main__':
    main()