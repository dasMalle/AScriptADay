using UnityEngine;
using System.Collections;

public class URLButton :MonoBehaviour {

    public string URL = "http://malenaklaus.de";
	public void OpenUrl()
    {
        Application.OpenURL(URL);
    }
}
