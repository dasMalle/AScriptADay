using UnityEngine;
using System.Collections;

public class GravitySwap : MonoBehaviour {

    Vector3 gravity;
    public bool swap = false;

    void Start()
    {
        gravity = Physics.gravity;
    }

    void FixedUpdate()
    {
        Physics.gravity = gravity;

        if (swap)
        {
            gravity.x = 0;
            gravity.y = -25;
            gravity.z = 0;
        }
    }
}
