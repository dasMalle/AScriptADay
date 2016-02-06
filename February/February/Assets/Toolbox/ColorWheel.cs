using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class ColorWheel : MonoBehaviour {

    public Color32 startColor;
    //public Image obj;
    public Camera obj;
    public float h = 0.2f;
    public Vector3 hsv;

    // Use this for initialization
	void Start () {
	}
	
	// Update is called once per frame
	void Update () {
        //transform.Translate(Input.acceleration.x, 0, -Input.acceleration.z);
        obj.backgroundColor = Color.HSVToRGB(h, 1, 1);
        if (h < 1)
        {
            h = h + Input.acceleration.x* 0.005f; 
        }
        else
        {
            h = 0;
        }
    }
}
