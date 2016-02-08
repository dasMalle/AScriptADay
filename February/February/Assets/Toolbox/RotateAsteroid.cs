using UnityEngine;
using System.Collections;

public class RotateAsteroid : MonoBehaviour {

    SpriteRenderer r;
    public Color firstColor, second;
    float t;
    public float speed;
	// Use this for initialization
	void Start () {
        r = GetComponent<SpriteRenderer>();
    }
	
	// Update is called once per frame
	void Update () {
        t = Mathf.PingPong(Time.time * speed, 1.0f);
        transform.Rotate(new Vector3(0,0, 30) * Time.deltaTime);
        if (r)
        {
            r.color = Color.Lerp(firstColor, second, t);
        }
    }
}
