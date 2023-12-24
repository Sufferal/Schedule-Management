import './styles/App.css';
import ButtonList from './components/ButtonList';
import Navbar from './components/Navbar';
import Preview from './components/Preview';
import Algorithm from './components/Algorithm';
import Footer from './components/Footer';
import './styles/App.css'

function App() {
  return (
    <div >
      <Navbar />
      <ButtonList />
      <Algorithm />
      <Footer />
    </div>
  );
}

export default App;
