/** author: Malena Klaus
*   date: 10.November 2015
*/
using UnityEngine;
using System.Collections;
using UnityEngine.UI;

//Todo: think if blocking should be a seperate script to make it easier for the ai
public class HealthBar : MonoBehaviour {

	[Range(0, 100)] public int CurrentHealth;
    private int initialHealth;
    public Slider healthSlider;
    private MoveControl control = null; //used for checking if the character blocks
    // Use this for initialization
	void Start ()
	{
	    initialHealth = 100;
	    healthSlider.maxValue = initialHealth;
	    healthSlider.minValue = 0;
        if (this.gameObject.GetComponent("MoveControl"))//careful, could be null, always check first
            control = this.gameObject.GetComponent<MoveControl>();

    }
	
	// Update is called once per frame
	void Update () {
        //Debug.Log("Health: "+ CurrentHealth);
	    healthSlider.value = CurrentHealth;
	}


        //keep in mind that in order for this to work the damaging object needs to be checked as trigger and needs a damage script directly attached
    void OnTriggerEnter(Collider obj)
    {
        var damage = obj.gameObject.GetComponent<Damage>();
        MoveControl opponentControl = obj.gameObject.GetComponentInParent<MoveControl>(); 


        if(control!= null)
        {
            if (damage != null && control.blockState != MoveControl.BlockState.Blocking)
            {
                if(opponentControl != null && opponentControl.attackState == MoveControl.AttackState.Attacking ) //only take damage when the opponent is actually attacking
                {
                    CurrentHealth = CurrentHealth - damage.CurrentDmg;
                    if (control.facingRight )
                        opponentControl.PushRight();
                    else if (!control.facingRight)
                    {
                        opponentControl.PushLeft();
                    }
                    else
                    { 
                        //wtf this shouldn't be
                    }
                }
                    
            }
        }
        else
        {
            if (damage != null)
                CurrentHealth = CurrentHealth - damage.CurrentDmg;
        }        
    }

    public void Reset()
    {
        CurrentHealth = initialHealth;
    }
}
