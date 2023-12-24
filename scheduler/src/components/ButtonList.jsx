import React, { useState } from 'react';
import axios from 'axios';
import '../styles/buttons.css';

const ButtonList = () => {
  const [file, setFile] = useState(false);
  const [convertClicked, setConvertClicked] = useState(false);
  const [downloadClicked, setDownloadClicked] = useState(false);
  const [isSuccessful, setIsSuccessful] = useState(false);

  function handleFileChange(e) {
    setFile(e.target.files[0]);
  }

  async function handleConvert() {
    setConvertClicked(true);

    if (!file) {
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/convert', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
      });

      console.log('Server response:', response.data);
      if (response.data.status === "success") {
        setIsSuccessful(true);
      }
    }
    catch (error) {
      console.error('Error uploading file:', error.message);
    }
  }

  async function handleDownload() {
    setDownloadClicked(true);

    if (!file || !isSuccessful) {
      return;
    }

     try {
      const response = await axios.get('http://localhost:5000/download', {
        responseType: 'blob', // Set the response type to blob
      });

      // Create a download link and trigger a click to download the file
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'output.xlsx');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (error) {
      console.error('Error downloading file:', error.message);
    }
  }

  return (
    <div >
      <h2 className='btn-heading'>Select a file to scan</h2>
      <input type="file" className='btn-wrapper' onChange={handleFileChange}  />
      {(convertClicked || downloadClicked) && !file && (
        <p className='error'>Please select a file to scan</p>
      )}
      {!convertClicked && downloadClicked && file && !isSuccessful && (
        <p className='error'>Please convert the file first</p>
      )}
      <div className="actions">
        <button className='btn-convert' onClick={handleConvert}>Convert</button>
        <button onClick={handleDownload}>Download</button>
      </div>
    </div>
  )
}

export default ButtonList