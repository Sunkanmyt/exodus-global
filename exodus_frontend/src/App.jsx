import { BrowserRoute, Routes, Route } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Sermons from '.pages/Sermons';

const Home = () => <div className="p-20 text-center text-4xl font-bold">Welcome to Exodus Global</div>;
const Gallery = () => <div className="p-20 text-center text-4xl font-bold">Gallery Coming Soon</div>;

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* The Layout wraps ALL these routes */}
        <Route path="/" element={<MainLayout />}>
          <Route index element={<Home />} />
          <Route path="sermons" element={<Sermons />} />
          <Route path="gallery" element={<Gallery />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;