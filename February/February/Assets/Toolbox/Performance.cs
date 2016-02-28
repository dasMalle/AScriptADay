using UnityEngine;
using System.Collections;

public class Performance : MonoBehaviour {

    // reducing getComponent calls

    Rigidbody2D rb;

    void Awake()
    {
        rb = (Rigidbody2D)GetComponent(typeof(Rigidbody2D)); //this executes faster than
        //rb = GetComponent<Renderer>().GetComponent<Collider>().GetComponent<Rigidbody>();
    }
    // Use this for initialization
    void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
