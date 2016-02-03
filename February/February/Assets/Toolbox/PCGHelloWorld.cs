using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class PCGHelloWorld : MonoBehaviour
{

    public Text str;
    public float interval = 1;
    public string[] hellos = new string[8] 
    {
      "Hello World", "Hola Mundo", "Bonjour Le Monde", "Hallo Welt", "Hej Verden", "Hej världen", "Selam Dünya", "Ciao mondo"
    };

    private float timer;
    
    void Start ()
    {
        str.text = "Hello World";
	}
	

	void Update ()
    {

        if(timer < Time.timeSinceLevelLoad)
        {
            Random.seed = (int)System.DateTime.Now.Ticks;
            int randomIndex = Random.Range(0, hellos.Length);
            str.text = hellos[randomIndex];
            timer = Time.timeSinceLevelLoad + interval;
        }
        
    }
}
