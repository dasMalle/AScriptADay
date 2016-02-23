using UnityEngine;
using System.Collections;

public class Teleport : MonoBehaviour
{
    public float range = 5.0f;

    void OnCollisionEnter(Collision col)
    {

        col.transform.position = Random.insideUnitSphere * 5;
    }
}
