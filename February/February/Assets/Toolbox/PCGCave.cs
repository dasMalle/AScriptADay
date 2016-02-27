using UnityEngine;
using System.Collections;

public class PCGCave : MonoBehaviour {

//Random tiles for today 
    public int[,] level;
    public int width, height = 30;

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

    public void Generate()
    {
        level = new int [width, height];

        for(int i = 0; i< width; i++)
        {
            for(int j = 0; j< height; j++)
            {
                level[i, j] = Random.Range(0, 1);
            }
        }
    }
}
