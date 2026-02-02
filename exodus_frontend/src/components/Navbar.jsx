import { NavLink } from "react-router-dom";

function Navbar() {
  const navStyle = ({ isActive }) =>
    isActive
      ? "text-exodus font-bold border-b-2 border-exodus"
      : "text-slate-600 hover:text-exodus transition-colors";

  return (
    <nav className="bg-white shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        {/* Ministry Logo Area */}
        <div className="text-2xl font-black tracking-tighter text-slate-900">
          EXODUS <span className="text-exodus">GLOBAL</span>
        </div>

        {/* Navigation Links */}
        <div className="space-x-8 text-sm uppercase tracking-widest font-medium">
          <NavLink to="/" className={navStyle}>
            Home
          </NavLink>
          <NavLink to="/sermons" className={navStyle}>
            Sermons
          </NavLink>
          <NavLink to="/gallery" className={navStyle}>
            Gallery
          </NavLink>
          <NavLink to="/partnership" className={navStyle}>
            Partnership
          </NavLink>
          <NavLink to="/contact" className={navStyle}>
            Contact
          </NavLink>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
