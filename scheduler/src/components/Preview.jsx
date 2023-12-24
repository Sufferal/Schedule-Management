import React from 'react'
import preview from '../images/preview.png'
import '../styles/preview.css'
import axios from 'axios'

const Preview = () => {
  async function handlePreview() {
    console.log('Preview')
    // Check if imgEl exists, if so, remove it
    if (document.querySelector('.centered-img')) {
      document.querySelector('.centered-img').remove()
    }
    
    const response = await axios.get('http://localhost:5000/preview', {
        responseType: 'blob', // Set the response type to blob
    });

    console.log(response.data)
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const imgEl = document.createElement('img');
    imgEl.src = url;
    imgEl.classList.add('centered-img'); 
      
    // Insert after the preview button
    const previewBtn = document.querySelector('.preview-btn');
    previewBtn.parentNode.insertBefore(imgEl, previewBtn.nextSibling);
  }

  return (
    <div className='preview'>
      <a className='preview-btn' href='#' onClick={handlePreview}>
        <img className='preview-img' src={preview} alt="preview" />
      </a>
      <button className='preview-title btn-preview' onClick={handlePreview}>Preview</button>
    </div>
  )
}

export default Preview