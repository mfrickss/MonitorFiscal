import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card from './Card'

function App() {
  return (
    <>
      <div className="painel">
        <h1>Monitor Fiscal Dashboard</h1>

        <div className="cards-container">
          <Card titulo="Dólar comercial" valor="5.15" />
          <Card titulo="Euro" valor="5.50" />
          <Card titulo="Bitcoin" valor="350.000" />
        </div>
      </div>
    </>
  )
}

export default App
