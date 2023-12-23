import React from 'react'
import logo from '../images/logo.png'
import '../styles/navbar.css'

const Navbar = () => {
  return (
    <nav className='navbar'>
      <img className='logo' src={logo} alt="logo" />
      <h2>OCR Handwriting Recognition</h2>
    </nav>
  )
}

export default Navbar