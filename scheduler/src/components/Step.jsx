import React from 'react'
import '../styles/step.css'

const Step = ({ title, description }) => {
  return (
    <div className='step'>
      <h2 className='step-title'>{title}</h2>
      <p className='step-desc'>{description}</p>
    </div>
  )
}

export default Step