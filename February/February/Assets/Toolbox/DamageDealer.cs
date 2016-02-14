using UnityEngine;
using System.Collections;

//[RequireComponent(Collider)]
public class DamageDealer : MonoBehaviour {

    [SerializeField]
    float dmg;
    [SerializeField]
    bool constantDmg;
    [SerializeField]
    float dmgCooldown;

    float timeSinceDmgDealt;

    // Use this for initialization
	void Start () {
	
	}
	
    void OnCollisionEnter(Collision col)
    {
        if(constantDmg || timeSinceDmgDealt > dmgCooldown)
        {
            var health = col.gameObject.GetComponent<Health>();
            if (health)
                health.Damage(dmg);
        }
    }
}
