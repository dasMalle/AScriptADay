using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class InputTest : MonoBehaviour {

    public Text text;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {

         text.text = Input.acceleration.z.ToString();
        if (Input.touchCount == 2)
        {
            text.text = "2 fingers on screen";
        }

        }
}
