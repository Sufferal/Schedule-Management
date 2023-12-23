import React from 'react'
import preview from '../images/preview.png'
import '../styles/preview.css'

const Preview = () => {
  return (
    <div className='preview'>
      <a className='preview-btn' href='#'>
        <img className='preview-img' src={preview} alt="preview" />
      </a>
      <h2 className='preview-title'>Preview</h2>
    </div>
  )
}

export default Preview