'use client'

import React, { useState } from 'react';
import axios from 'axios';
import { Gallery } from "react-grid-gallery";

const Dalle = () => {
  const [keyword, setKeyword] = useState('');
  const [numberOfImages, setNumberOfImages] = useState('');
  const [loading, setLoading] = useState(false); // State variable for loading status
  const [images, setImages] = useState([]); // State variable for images
  const [selectedImagePaths, setSelectedImagePaths] = useState([]); // State variable for selected image paths
  const [zipGenerated, setZipGenerated] = useState(false);
  const [downloadLink, setDownloadLink] = useState();


  const httpServer = "http://localhost:5001/"; // This is the development http server on port 5001

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true); // Set loading to true when the request is initiated

    const numImagesAsNumber = parseInt(numberOfImages); // Sending number of images as a number

    const requestBody = {
      "keyword": keyword,
      "num_images": numImagesAsNumber
    };

    // Log the request body
    console.log('Request Body:', requestBody);

    try {
      const response = await axios.post('http://127.0.0.1:5000/dalle', requestBody);
      
      // Handle success response
      console.log('Images generated successfully:', response.data);
      setLoading(false); // Set loading to false when the response is received
      // Set the images state with the images received from the backend
      console.log(response.data.image_paths)
      // THIS PART MIGHT NEED MODIFICATION WHEN DEPLOYED
      setImages(response.data.image_paths.map(imagePath => ({
        src: `${httpServer}${imagePath.replace('/home/pyslarash/Documents/code/aiartonacob/api/', '')}`,
        width: 300, // Set thumbnail width as needed
        height: 300, // Set thumbnail height as needed
      })));
      setZipGenerated(false); // Reset zip generation flag
    } catch (error) {
      console.error('Error generating images:', error.message);
      setLoading(false); // Set loading to false in case of an error
    }
  };

  const hasSelected = images.some((image) => image.isSelected);

  const handleSelect = (index) => {
    const nextImages = images.map((image, i) =>
      i === index ? { ...image, isSelected: !image.isSelected } : image
    );
    setImages(nextImages);

    const selectedPaths = nextImages.filter(image => image.isSelected).map(image => image.src);
    setSelectedImagePaths(selectedPaths);
    console.log("Selected:", selectedPaths);
  };

  const handleSelectAllClick = () => {
    const nextImages = images.map((image) => ({
      ...image,
      isSelected: !hasSelected,
    }));
    setImages(nextImages);

    const selectedPaths = nextImages.filter(image => image.isSelected).map(image => image.src);
    setSelectedImagePaths(selectedPaths);
    console.log("Selected:", selectedPaths);
  };


  const openImageInNewWindow = (index) => {
    window.open(images[index].src, '_blank');
  };

  const generateZip = async (selectedImagePaths) => {
    const apiPath = '/home/pyslarash/Documents/code/aiartonacob/api';
    const zipEndpoint = 'http://localhost:5000/zip';
  
    const pathsWithoutServer = selectedImagePaths.map(path => {
      const url = new URL(path);
      return apiPath + url.pathname;
    });
  
    const requestBody = {
      image_paths: pathsWithoutServer,
    };
  
    console.log('Request Payload:', requestBody); // Logging the payload
  
    try {
      const response = await axios.post(zipEndpoint, requestBody);
      // Handle success response, e.g., show a success message or trigger the download
      console.log('ZIP file created:', response.data);
      setZipGenerated(true);
      setDownloadLink(httpServer + response.data.zip_file_path)
    } catch (error) {
      // Handle error response
      console.error('Error creating ZIP file:', error.message);
    }
  };

  return (
    <div className="flex w-full">
      <div className="w-1/3 mr-5 p-2">
        <form onSubmit={handleSubmit} className="flex flex-col items-center">
          <input
            type="text"
            placeholder="Keyword"
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
            className="w-full border border-gray-300 rounded-md p-2 mb-4 text-black"
          />
          <input
            type="number"
            placeholder="Number of images"
            value={numberOfImages}
            onChange={(e) => setNumberOfImages(e.target.value)}
            className="w-full border border-gray-300 rounded-md p-2 mb-4 text-black"
          />
          <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Generate
          </button>
        </form>
      </div>

      <div className="w-2/3 p-2">
        {loading ? (
          <div className="text-center mt-6">
            <div role="status">
              <svg aria-hidden="true" className="inline w-10 h-10 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
              </svg>
              <span className="sr-only">Loading...</span>
            </div>
          </div>
        ) : (
          images.length > 0 && (
            <div>
              <div className="p-t-1 p-b-1">
                <button onClick={handleSelectAllClick}>
                  {hasSelected ? "Clear selection" : "Select all"}
                </button>
                {hasSelected && (
                  <span> | </span>
                )}
                {hasSelected && (
                  zipGenerated ? (
                    <a href={downloadLink} download>
                      <button>Download ZIP</button>
                    </a>
                  ) : (
                    <button onClick={() => generateZip(selectedImagePaths)}>Generate ZIP</button>
                  )
                )}
              </div>
              <Gallery images={images} onSelect={handleSelect} onClick={openImageInNewWindow} />
            </div>
          )
        )}
      </div>
    </div>
  );
};

export default Dalle;