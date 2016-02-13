using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.EventSystems;

[RequireComponent(typeof(Scrollbar))]
public class ProgressBar : MonoBehaviour {

    [SerializeField]
    Image CircleImage;

    [SerializeField]
    [Range(0, 1)]
    float filled = 100;

    [SerializeField]
    bool animate = true;
    float waitTime = 30.0f;

    Scrollbar scrollbar { get { return GetComponent<Scrollbar>(); } }

    void Start()
    {
        CircleImage.type = Image.Type.Filled;
        CircleImage.fillMethod = Image.FillMethod.Radial360;
        CircleImage.fillOrigin = 0;
    }

    void Update()
    {        
        CircleImage.fillAmount = filled;
        if(animate)
        {
            CircleImage.fillAmount -= 1.0f / waitTime * Time.deltaTime;
        }
        filled = CircleImage.fillAmount;
    }

}
