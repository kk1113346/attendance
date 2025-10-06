System;
System.Text;
 
class Program
{
    static string EncryptAsciiPlus5(string s)
    {
        var sb = new StringBuilder(s.Length);
        foreach (char c in s)
        {
            sb.Append(c == ' ' ? c : (char)(c + 5));
        }
        return sb.ToString();
    }
 
    static string DecryptAsciiMinus5(string s)
    {
        var sb = new StringBuilder(s.Length);
        foreach (char c in s)
        {
            sb.Append(c == ' ' ? c : (char)(c - 5));
        }
        return sb.ToString();
    }
 
    static void Main()
    {
        string text = "I asked Alicia and Ian about an algorithmic approach: analyse input arrays, iterate intelligently, and adapt as anomalies arise.";
        string enc = EncryptAsciiPlus5(text);
        string dec = DecryptAsciiMinus5(enc);
 
        Console.WriteLine("Original:");
        Console.WriteLine(text);
        Console.WriteLine("\nEncrypted (ASCII + 5, spaces preserved):");
        Console.WriteLine(enc);
        Console.WriteLine("\nDecrypted (check):");
        Console.WriteLine(dec);
    }
}