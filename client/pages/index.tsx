import React, {useEffect, useState} from 'react'
import MarketData from './components/MarketData'
import NavBar from './components/NavBar'
import EarningsReport from './components/EarningsReport'

function index() {
  return (
    <div>
      <NavBar/>
      <MarketData/>
      <EarningsReport/>
    </div>
  )
}

export default index
