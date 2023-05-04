package saagnik;
import java.io.Serializable;

// To persist the data for future use,
// implement serializable
public class ValidateUser implements Serializable {
	private String user, pass;

	// Methods to set username and password
	// according to form data
	public void setUser(String u1) { this.user = u1; }
	public void setPass(String p1) { this.pass = p1; }

	// Methods to obtain back the values set
	// by setter methods
	public String getUser() { return user; }
	public String getPass() { return pass; }

	// Method to validate a user
	public boolean validate(String u1, String p1)
	{
		if (u1.equals(user) && p1.equals(pass))
			return true;
		else
			return false;
	}
}
