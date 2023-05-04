<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
       <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
       <title>Login Page</title>
    </head>
    <body>
        <h1>User Details</h1>
        <%-- The form data will be passed to acceptuser.jsp 
             for validation on clicking submit
        --%> 
        <form method ="get" action="acceptuser.jsp">
            Enter Name : <input type="text" name="user"><br/><br/>
            Enter Mobile Number : <input type="Number" name ="user"><br/></br>
            Enter Email Id: <input type="text" name ="user"><br/></br>
                <input type ="submit" value="LOGIN">    
        </form>
    </body>
</html>
	
