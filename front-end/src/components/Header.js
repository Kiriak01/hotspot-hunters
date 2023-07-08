import logo from './images/logo.png';
import classes from './Header.module.css';
import 'reactjs-popup/dist/index.css';
import { useState } from 'react';
import Login from '../components/Login'
import Register from './Register'
 


function Header ()  {

    const [openpopuplogin, setvaluelogin] = useState(false);
    const [openpopupregister, setvalueregister] = useState(false);

    return(
        <header className={classes.t3}>
            <div className={classes.header} >
            <img src={logo} width={200} height={200} />
                <nav>
                    <ul>
                        <li>Home</li>
                        <li>Contact</li>
                        <li>Info</li>
                        <button onClick={ () => setvalueregister(true)}
                        >Register</button> 
                        <button onClick={ () => setvaluelogin(true)}
                        >Login</button>

                    </ul>
                </nav>
            </div>
            <div className={classes.header1} >
               
                <h2 className={classes.t2}>FREE WIFI</h2>
                <Login open={openpopuplogin}
                        onClose={ ()=>setvaluelogin(false)} />
                <Register open={openpopupregister}
                        onClose={ ()=>setvalueregister(false)} />       
            </div>



        </header>

    );
};

export default Header;