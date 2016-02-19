using UnityEngine;
using System.Collections;

public class FSM : MonoBehaviour {

    private State currentState;

    public void SwitchState(State newState)
    {
        currentState.EndState(this);
        currentState = newState;
        currentState.BeginState(this);
    }

    void Update()
    {
        if (currentState != null)
        {
            currentState.UpdateState(this);
        }
    }
}

public abstract class State
{
    public abstract void BeginState(FSM fsm);
    public abstract void UpdateState(FSM fsm);
    public abstract void EndState(FSM fsm);
}
