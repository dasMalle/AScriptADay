using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using System.Collections.Generic;

public class CC2016 : MonoBehaviour {


    public Text debugLine;
    private List<string> beers = new List<string>();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
	// Use this for initialization
	void Start () {
        beers.Add("Jever");
        beers.Add("Leffe");
        beers.Add("Becks");
        beers.Add("Walhalla");
        beers.Add(" Warsteiner");
        beers.Add(" Tuborg");
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.B)) {
           var nextBeer =  Random.Range(0, beers.Count);
            debugLine.text = beers[nextBeer];
        }
	}
}
