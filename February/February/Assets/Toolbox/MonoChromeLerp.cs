using UnityEngine;
using System.Collections;

public class MonoChromeLerp : MonoBehaviour {
    [SerializeField]
    Camera cam;
    Color start, end;
    public Color newColor;
    public bool next;
    float t = 0f;
   

    // Use this for initialization
    void Start () {
        next = false;
	}
	
	// Update is called once per frame
	void Update () {

        if (next && newColor != cam.backgroundColor)
        {
            start = newColor;
            end = nextColor(start);
            next = false;
            t = 0;
        }
        cam.backgroundColor = Color.Lerp(start, end, t);
        t += Time.deltaTime;

    }

    public Color nextColor(Color c)
    {
        float h, s, v;
        Color.RGBToHSV(c, out h, out s, out v);
        if (s > 0.5)
        {
            return Color.HSVToRGB(h, Random.Range(0.5f, 1.0f), v);
        }
        else
            return Color.HSVToRGB(h, Random.Range(0.0f, 0.5f), v);
    }
}
