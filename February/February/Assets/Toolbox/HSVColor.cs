using UnityEngine;
using System.Collections;

public class HSVColor  {

//this will be the base for monochrome fluid colors
    public Vector3 RGBToHSV( Color c)
    {
        float max = System.Math.Max(c.r, System.Math.Max(c.g, c.b));
        float min = System.Math.Min(c.r, System.Math.Min(c.g, c.b));
        float l = max + min / 2; //calculates luminace
        float s, h;
        if(min != max) //otherwise no saturation 
        {
            if (l < 0.5)
                s = (max - min) / (max + min);
            else
                s = (max - min)/(2.0f - max - min);
            if (max == c.r)
                h = (c.g - c.b) / (max - min);
            else if (max == c.g)
                h = 2.0f + (c.b - c.r) / (max - min);
            else
                h = 4.0f + (c.r - c.g) / (max - min);
            h = h * 60; //convert to degrees on the color cycle
        }
        else
        {
            s = 0;
            h = 0;
        }
        return new Vector3(h, s, l);
    }
}
