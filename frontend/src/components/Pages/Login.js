import React from 'react';


function Login() {
    return (
        <form>
            <div className="form-inner">
                <h2>Login</h2>

                <div className="form-group">
                    <label htmlFor="username">Username:</label>
                    <input type="text" name="username" id="username"/>
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password:</label>
                    <input type="password" name="password" id="password"/>
                </div>
                <input type="submit" value="login"/>
            </div>





        </form>
    )
}

export default Login
