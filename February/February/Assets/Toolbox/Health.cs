using UnityEngine;
using System.Collections;

public class Health : MonoBehaviour {

    [SerializeField]
    float currHealth;
    [SerializeField]
    float maxHealth;
    // Use this for initialization
	
    public void Damage(float dmg)
    {
        if (currHealth > dmg)
            currHealth -= dmg;
        else
            Debug.Log("dead");
    }
}
