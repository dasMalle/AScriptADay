using UnityEngine;
using System.Collections;

public class MoveShip : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
#if UNITY_EDITOR
        transform.Translate(Input.GetAxis("Horizontal") * 0.5f, Input.GetAxis("Vertical") *0.5f, 0);

    #elif UNITY_ANDROID

        transform.Translate(Input.acceleration.x *0.5f, Input.acceleration.y*0.5f, 0);
    #endif
    }
}
