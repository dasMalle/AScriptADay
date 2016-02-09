using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class AsteroidSpawn : MonoBehaviour {

    public GameObject centrum;
    public GameObject[] objs;
    public int maxCount;
    public float range;


    private List<GameObject> objInstances = new List<GameObject>();
    // Use this for initialization
	void Start () {

	}
	
	// Update is called once per frame
	void Update () {
        if (objs.Length >= 1)
        {
            if (objInstances.Count < maxCount)
            {
                var pos = getPosition();
                GameObject asteroid = Instantiate(objs[Random.Range(0, objs.Length)], pos, transform.rotation) as GameObject;
                objInstances.Add(asteroid);
            }
            else
            {
                Debug.Log("checking");
                for(int i = 0; i < objInstances.Count; i++)
                {
                    checkDistance(objInstances[i]);
                }
                    
            }
        }
        else
            Debug.Log("no instatiatable object reference in Asteroid Spawn");      
	}

    public void checkDistance(GameObject obj)
    {
        
        if(System.Math.Abs( Vector3.Distance(centrum.transform.position, obj.transform.position)) > range){
            obj.transform.position = getPosition();
            Debug.Log("moved asteroid");
        }            
    }

    private Vector3 getPosition()
    {
        return centrum.transform.position + Random.insideUnitSphere * range + new Vector3(range, range, 0);
    }

    public int AsteroidCount()
    {

        return objInstances.Count;
    }
}
