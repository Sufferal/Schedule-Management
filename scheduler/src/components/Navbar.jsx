import React from 'react'
import logo from '../images/star.png'
import '../styles/navbar.css'


const Navbar = () => {
  return (
    <nav className='navbar'>
      <img className='logo' src={logo} alt="logo" />
      <h2 className='navbar-title'>Perfect Pixel</h2>
    </nav>
  )
}

export default Navbar