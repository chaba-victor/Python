# Automated Image Resizer
Images are pivotal in web development, often contributing to captivating user experiences. However, they can also be the prime culprits in website slowdowns, especially if they’re not optimized for the plethora of devices accessing the web today. To tackle this, automating the process of resizing and optimizing images is essential. 

## Script Overview
The Python script discussed here harnesses the Python Imaging Library (PIL) to adeptly manage images. It follows these principal steps:

1. Scour a designated directory for images.
2. Clean up image names by substituting spaces with hyphens.
3. Resize images based on specified breakpoints for different devices.
3. Store the images in both the standard JPEG/PNG and the more efficient WebP formats.
4. Generate a `picture` HTML tag with multiple `source` elements catering to each breakpoint.


The `picture_tag.txt` will have the picture tag all ready for you like this..
 
 ```html
<picture>
    <source srcset="anime-meme_xs.webp 1x, anime-meme_xs.jpg 1x" media="(max-width: 400px)">
    <source srcset="anime-meme_sm.webp 1x, anime-meme_sm.jpg 1x" media="(max-width: 640px)">
    <source srcset="anime-meme_md.webp 1x, anime-meme_md.jpg 1x" media="(max-width: 768px)">
    <source srcset="anime-meme_lg.webp 1x, anime-meme_lg.jpg 1x" media="(min-width: 769px)">
    <img src="anime-meme_lg.jpg" alt="...">
</picture>

```
Don’t forget to update the `alt` attribute!


## Prerequisites and Execution Guide
To utilize the Python script efficiently for automated image resizing, ensure you have the prerequisites in place and follow the execution steps listed below.

### Prerequisites:
Python: Ensure you have Python 3.x installed. You can verify this by running:

    python --version
**Python Imaging Library (PIL)**: The script depends on PIL (often available via the Pillow package). If not already installed, you can add it using pip:

    pip install Pillow
**Directory Structure**: The script anticipates two main directories:

- `input`: This should contain the images you wish to resize.
- `output`: This is where the script will save the resized images and generated picture tags. (The script will automatically create this directory if it doesn't exist.)

**Supported Image Formats**: Currently, the script is designed to process `.jpg`, `.jpeg`, and `.png` files. Ensure the images you wish to process are in one of these formats.

**Running the Script**:
- **Script Placement**: Place the Python script in a location where the `input` directory resides.
- **Populate the Input Directory**: Ensure all the images you want to resize are inside the input directory.
- **Execute the Script**: Navigate to the script’s directory using a terminal or command prompt and run:

        python Sizer.py


1. **Review the Output**: Post-execution, navigate to the output directory. Here you'll find the resized images, organized in individual folders named after the original image's sanitized name. Each folder will also contain a picture_tag.txt file, which includes the appropriate HTML picture tag to utilize the resized images on a webpage.

2. **Savings Information**: After the script completes its run, it will display the total storage savings in MBs directly in the terminal or command prompt.


By adhering to these prerequisites and steps, you’ll ensure a smooth execution of the script, optimizing your images for web usage seamlessly.

## Pre-set Parameters and Breakpoints
The script has pre-configured settings:

- `INPUT_DIR`: Directory housing the original images.
- `OUTPUT_DIR`: Directory where processed images and the associated picture tags get stored.
- `QUALITY`: Desired quality for saved images.
- `BREAKPOINTS`: A dictionary pairing device breakpoints with their respective widths.
## Core Functions
1. `name_sanitizer()`

This function gives images web-friendly names by swapping out spaces for hyphens.

2. `resize_image()`

This function resizes an image according to a given breakpoint, then saves it in both JPEG/PNG and WebP formats, informing if the image was indeed resized.

## Main Routine
In the primary routine:

1. **Image Ingestion**: The script identifies all image files (JPEGs and PNGs) in the INPUT_DIR.
2. **Backup Procedure**: Every image is first backed up before any processing commences.
3. **Resizing and Storing**: For each breakpoint, if an image’s width surpasses the breakpoint’s limit, it’s resized and stored in the designated format.
4. **Crafting Picture Tags**: For every resized image, source tags are produced. These tags are then amalgamated to formulate a picture tag. The resulting tag is stored in a text file, ready to be integrated into a web page.
5. **Computing Savings**: A summation of storage savings is computed by comparing the original image size against the cumulative size of the resized ones.
## Deployment
On executing the script, it trawls through all images in the `INPUT_DIR`, places the optimized versions in the `OUTPUT_DIR`, and exhibits the storage savings in MBs.