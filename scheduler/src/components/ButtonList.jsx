import React from 'react'
import '../styles/buttons.css'

const ButtonList = () => {
  return (
    <div >
      <h2 className='btn-heading'>Select a file to scan</h2>
      <input type="file" className='btn-wrapper'/>
      
      <div className="actions">
        <button>Convert</button>
        <button>Download</button>
      </div>
    </div>
  )
}

export default ButtonList