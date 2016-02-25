using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class Clock : MonoBehaviour {

    public Text t;
    
    // Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {

        var time = System.DateTime.Now;
        t.text= string.Format(" {0}:{1}:{2}",  time.Hour, time.Minute, time.Second);
    }
}
