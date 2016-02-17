using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using System.Collections.Generic;

public class ButtonSoundManager : MonoBehaviour {
    
    public AudioClip a;
    public AudioSource source;
    // Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

    public void playSound()
    {
        source.PlayOneShot(a); 
    }
}
