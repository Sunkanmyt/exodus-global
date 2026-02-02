import { Outlet } from 'react-router-dom';
import Navbar from '../components/Navbar';

function MainLayout() {
    return (
        <div className='flex flex-col min-h-screen'>
            {/* Navbar for the top */}
            <Navbar/>

            {/* The placeholder for the body pages */}
            <main className='flex-grow'>
                <Outlet/>
            </main>

            {/* The footer for the base */}
            <Footer className='bg-slate-900 text-white p-8 text-center'>
                <p>&copy; 2026 Exodus Global. The move is here!</p>
            </Footer>
        </div>
    );
}

export default MainLayout;