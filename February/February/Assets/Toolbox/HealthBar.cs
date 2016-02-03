/** author: Malena Klaus
*   date: 01.02.16 
*   super easy health bar by using unity ui slider
*/
using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class HealthBar : MonoBehaviour {

	[Range(0, 100)] public int CurrentHealth;
    private int initialHealth;
    public Slider healthSlider;
    public int damage;  //replace this by a damage script attached to the damaging gameobject
	void Start ()
	{
	    initialHealth = 100;
	    healthSlider.maxValue = initialHealth;
	    healthSlider.minValue = 0;       

    }
	
	// Update is called once per frame
	void Update () {
	    healthSlider.value = CurrentHealth;
	}


        //keep in mind that in order for this to work the damaging object needs to be checked as trigger and needs a damage script directly attached
    void OnTriggerEnter(Collider obj)
    {

        CurrentHealth = CurrentHealth - damage;
                    
    }

    public void Reset()
    {
        CurrentHealth = initialHealth;
    }
}
