using UnityEngine;
using System.Collections;

public class LevelManager : MonoBehaviour {

    [SerializeField]
    GameObject Player;

    public static LevelManager instance = null;

    // Use this for initialization
    void Start () {
        if (!Player)
            Debug.Log("LevelManager is missing Player reference");
	}
    

    void Awake()
    {
        if (instance == null)            
            instance = this;
        
        else if (instance != this)
            Destroy(gameObject);
        
        DontDestroyOnLoad(gameObject);
    }

    // Update is called once per frame
    void Update () {
	
	}

    
}
