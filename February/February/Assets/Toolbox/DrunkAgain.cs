using UnityEngine;
using System.Collections;

public class DrunkAgain : MonoBehaviour {

    public GameObject l;
    public bool on = true;
    // Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
        if (l)
        {
            toggleLight(on);
        }
    }

    public void toggleLight(bool on)
    {
        if(on)
                l.SetActive(true);

        else
           l.SetActive(false);
    }
    
}
