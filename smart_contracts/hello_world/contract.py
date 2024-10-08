from pyteal import *
from beaker import *

class XRayChoreographyState:
    
    e0 = GlobalStateValue(stack_type=TealType.uint64, default=Int(1))
    e1 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e2 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e3 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e4 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e5 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e6 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e7 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e8 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e9 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e10 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e11 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e12 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e13 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e14 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e15 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e16 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e17 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e18 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    e19 = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))

    
    enabled_messages = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))

    ward= Addr("GDMVSGQMZKUDMIJ54RCMBGSW7YK6N53QYBS74UC3MIGT7EBR4VKEUAOHIE")
    Patient= Addr("RGKMCAKVBEPGKTJIMF4W7NIJIACKCL2XZGSRQXX3V4FXGDK6D2CXPZC5SM")
    radiology=Addr("D5NCMATCVMWGZ7S6VZZKRZJKRENF22L7FFGSKXHX2PDSDAR3G6C6N2VUJE")

    # Define state variables for various message statuses and payloads
    status_appointment = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_appointment = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_request = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_request = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_response = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_response_accepted = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_response_date = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_registration = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_registration_date = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    payload_registration_appointmentId = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_certification = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_certification = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_temperature = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_temperature = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_checkin = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_checkin = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_confirmation = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_confirmation = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    status_analysis = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_analysis = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))
    status_report = GlobalStateValue(stack_type=TealType.uint64, default=Int(0))
    payload_report = GlobalStateValue(stack_type=TealType.bytes, default=Bytes(""))


# Instantiate the application with the state
app = Application("XRayChoreography", state=XRayChoreographyState())



@app.create(bare=True)
def create() -> Expr:
    return app.initialize_global_state()

# Define the subroutines
@Subroutine(TealType.uint64)
def start1():
    return Seq(
        If(app.state.e0.get() > Int(0)).Then(
            Seq(
                app.state.e0.set(Int(0)),  
                app.state.e1.set(app.state.e1.get() + Int(1)),
                Int(1) 
            )
        ).Else(
            Int(0)  
        )
    )


@Subroutine(TealType.uint64)
def take_appointment():
    return Seq(
        If(app.state.e1.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Message"), Bytes("Patient 'radiology': appointment")),
                app.state.e1.set(app.state.e1.get() - Int(1)),
                app.state.status_appointment.set(Int(1)), 
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )

@app.external
def appointment(payload: abi.String):
    return Seq(
        If(app.state.status_appointment.get() == Int(1)).Then(
            Seq(
                app.state.payload_appointment.set(payload.get()), 
                app.state.status_appointment.set(Int(0)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),  
                app.state.e2.set(app.state.e2.get() + Int(1)),  
                execute()  
            )
        ).Else(
            Reject()
        )
    )

@Subroutine(TealType.uint64)
def xor1():
    return Seq(
        If(app.state.e2.get() > Int(0)).Then(
            Seq(
                app.state.e2.set(app.state.e2.get() - Int(1)),
                app.state.e3.set(app.state.e3.get() + Int(1)),
                Int(1)  
            )
        ).ElseIf(app.state.e6.get() > Int(0)).Then(
            Seq(
                app.state.e6.set(app.state.e6.get() - Int(1)),
                app.state.e3.set(app.state.e3.get() + Int(1)),
                Int(1)  
            )
        ).Else(
            Int(0) 
        )
    )

@Subroutine(TealType.uint64)
def check_availability():
    return Seq(
        If(app.state.e3.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Message"), Bytes("radiology 'ward': request")),
                app.state.e3.set(app.state.e3.get() - Int(1)),
                app.state.status_request.set(Int(1)),  # ENABLED
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )

@app.external
def request(payload: abi.String):
    return Seq(
        If(
            app.state.status_request.get() == Int(1),
              
        ).Then(
            Seq(
                #App.globalPut(Bytes("Message"), Bytes("Message 'request': received")),
                app.state.payload_request.set(payload.get()),
                app.state.status_request.set(Int(0)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),
                app.state.e4.set(app.state.e4.get() + Int(1)),
                execute(),
            )
        ).Else(
            Reject()
        )
    )


@Subroutine(TealType.uint64)
def check_availability_resp():
    return Seq(
        If(app.state.e4.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("ward, radiology ,response")),
                app.state.e4.set(app.state.e4.get() - Int(1)),
                app.state.status_response.set(Int(1)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),
                Int(1),
            )
        ).Else(
           Int(0)
        )
    )

@app.external
def response(payload: abi.Uint64, payload1: abi.String):
    return Seq(
        If(
            app.state.status_response.get() == Int(1),
              
        ).Then(
            Seq(  
                app.state.payload_response_accepted.set(payload.get()),
                app.state.payload_response_date.set(payload1.get()),  
                app.state.status_response.set(Int(0)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),
                app.state.e5.set(app.state.e5.get() + Int(1)),
                execute()
            )
        ).Else(
            Reject()
        )
    )
@Subroutine(TealType.uint64)
def xor2():
    return Seq(
        If(And(app.state.e5.get() > Int(0), app.state.payload_response_accepted.get() == Int(0))).Then(
            Seq(
                app.state.e5.set(app.state.e5.get() - Int(1)),
                app.state.e6.set(app.state.e6.get() + Int(1)),
                execute(),
                Int(1)  
            )
        ).ElseIf(And(app.state.e5.get() > Int(0), app.state.payload_response_accepted.get() == Int(1))).Then(
            Seq(
                app.state.e5.set(app.state.e5.get() - Int(1)),
                app.state.e7.set(app.state.e7.get() + Int(1)),
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )

@Subroutine(TealType.uint64)
def confirm_appointment():
    return Seq(
        If(app.state.e7.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("radiology, patient, registration")),
                app.state.e7.set(app.state.e7.get() - Int(1)),
                app.state.status_registration.set(Int(1)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )
@app.external
def registration(payload: abi.String,payload1:abi.String):
    return Seq(
        If(
            app.state.status_registration.get() == Int(1),  
              
        ).Then(
            Seq(
                app.state.payload_registration_date.set(payload.get()),  
                app.state.payload_registration_appointmentId.set(payload1.get()),  
                app.state.status_registration.set(Int(0)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),  
                app.state.e8.set(app.state.e8.get() + Int(1)),  
                execute()  
            )
        ).Else(
            Reject()  
        )
    )
@Subroutine(TealType.uint64)
def and1():
    return Seq(
        If(app.state.e8.get() > Int(0)).Then(
            Seq(
                app.state.e8.set(app.state.e8.get() - Int(1)),
                app.state.e9.set(app.state.e9.get() + Int(1)),  
                app.state.e10.set(app.state.e10.get() + Int(1)),  
                Int(1) 
            )
        ).Else(
            Int(0) 
        )
    )
@Subroutine(TealType.uint64)
def check_certification():
    return Seq(
        If(app.state.e9.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("radiology, patient, Certification")),
                app.state.e9.set(app.state.e9.get() - Int(1)), 
                app.state.status_certification.set(Int(1)), 
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),  
                Int(1) 
            )
        ).Else(
            Int(0)  
        )
    )
@app.external
def certification(payload: abi.String):
    return Seq(
        If(
            app.state.status_certification.get() == Int(1), 
             
        ).Then(
            Seq(
                
                app.state.payload_certification.set(payload.get()),  
                app.state.status_certification.set(Int(0)), 
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)), 
                app.state.e11.set(app.state.e11.get() + Int(1)),  
                execute()  
            )
        ).Else(
            Reject()  
        )
    )
@Subroutine(TealType.uint64)
def check_temperature():
    return Seq(
        If(app.state.e10.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("radiology, patient, temperature")),
                app.state.e10.set(app.state.e10.get() - Int(1)), 
                app.state.status_temperature.set(Int(1)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),  
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )
@app.external
def temperature(payload: abi.String):
    return Seq(
        If(
            app.state.status_temperature.get() == Int(1),   
        ).Then(
            Seq(
                app.state.payload_temperature.set(payload.get()), 
                app.state.status_temperature.set(Int(0)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),  
                app.state.e12.set(app.state.e12.get() + Int(1)),  
                execute() 
            )
        ).Else(
            Reject()  
        )
    )
@Subroutine(TealType.uint64)
def and2():
    return Seq(
        If(And(app.state.e11.get() > Int(0), app.state.e12.get() > Int(0))).Then(
            Seq(
                app.state.e11.set(app.state.e11.get() - Int(1)),  
                app.state.e12.set(app.state.e12.get() - Int(1)), 
                app.state.e13.set(app.state.e13.get() + Int(1)), 
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )
@Subroutine(TealType.uint64)
def check_in():
    return Seq(
        If(app.state.e13.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("radiology, patient, checkin")),
                app.state.e13.set(app.state.e13.get() - Int(1)),  
                app.state.status_checkin.set(Int(1)), 
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),  
                Int(1) 
            )
        ).Else(
            Int(0) 
        )
    )
@app.external
def checkin(payload: abi.String):
    return Seq(
        If(
            app.state.status_checkin.get() == Int(1),   
        ).Then(
            Seq(
                app.state.payload_checkin.set(payload.get()), 
                app.state.status_checkin.set(Int(0)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),  #
                app.state.e14.set(app.state.e14.get() + Int(1)),  
                execute()  
            )
        ).Else(
            Reject()  
        )
    )
@Subroutine(TealType.uint64)
def check_in_resp():
    return Seq(
        If(app.state.e14.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("radiology, patient, confirmation")),
                app.state.e14.set(app.state.e14.get() - Int(1)), 
                app.state.status_confirmation.set(Int(1)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),  
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )
@app.external
def confirmation(payload: abi.Uint64):
    return Seq(
        If(
            app.state.status_confirmation.get() == Int(1),   
        ).Then(
            Seq( 
                app.state.payload_confirmation.set(payload.get()),  
                app.state.status_confirmation.set(Int(0)), 
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),  
                app.state.e15.set(app.state.e15.get() + Int(1)),  
                execute()  
            )
        ).Else(
            Reject()  
        )
    )
@Subroutine(TealType.uint64)
def xor3():
    return Seq(
        If(And(app.state.e15.get() > Int(0), app.state.payload_confirmation.get() == Int(1))).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("Execution of xor3 element e16 branch")),
                app.state.e15.set(app.state.e15.get() - Int(1)),
                app.state.e16.set(app.state.e16.get() + Int(1)),
                Int(1)  # Return success
            )
        ).ElseIf(And(app.state.e15.get() > Int(0), app.state.payload_confirmation.get() == Int(0))).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("Execution of xor3 element e17 branch")),
                app.state.e15.set(app.state.e15.get() - Int(1)),
                app.state.e17.set(app.state.e17.get() + Int(1)),
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )


# End task 1
@Subroutine(TealType.uint64)
def end1():
    return Seq(
        If(app.state.e17.get() > Int(0)).Then(
            Seq(
                app.state.e17.set(app.state.e17.get() - Int(1)),  # Decrease e17
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )

@Subroutine(TealType.uint64)
def perform_xrays():
    return Seq(
        If(app.state.e16.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("radiology, ward, analysis")),
                app.state.e16.set(app.state.e16.get() - Int(1)),  
                app.state.status_analysis.set(Int(1)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),  
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )

# Handle analysis message
@app.external
def analysis(payload: abi.String):
    return Seq(
        If(
            app.state.status_analysis.get() == Int(1),
              
        ).Then(
            Seq(
                app.state.payload_analysis.set(payload.get()),
                app.state.status_analysis.set(Int(0)),  # DISABLED
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),
                app.state.e18.set(app.state.e18.get() + Int(1)),
                execute()
            )
        ).Else(
            Reject()
        )
    )

@Subroutine(TealType.uint64)
def send_result():
    return Seq(
        If(app.state.e18.get() > Int(0)).Then(
            Seq(
                App.globalPut(Bytes("Execution"), Bytes("ward, patient, report")),
                app.state.e18.set(app.state.e18.get() - Int(1)),  
                app.state.status_report.set(Int(1)),  
                app.state.enabled_messages.set(app.state.enabled_messages.get() + Int(1)),  
                Int(1)  
            )
        ).Else(
            Int(0)  
        )
    )

# Handle report message
@app.external
def report(payload: abi.String):
    return Seq(
        If(
            app.state.status_report.get() == Int(1),
              
        ).Then(
            Seq(
                App.globalPut(Bytes("Message"), Bytes("Message 'report': received")),
                app.state.payload_report.set(payload.get()),
                app.state.status_report.set(Int(0)),  # DISABLED
                app.state.enabled_messages.set(app.state.enabled_messages.get() - Int(1)),
                app.state.e19.set(app.state.e19.get() + Int(1)),
                execute()
            )
        ).Else(
            Reject()
        )
    )

@Subroutine(TealType.uint64)
def end2():
    return Seq(
        If(app.state.e19.get() > Int(0)).Then(
            Seq(
                 
                app.state.e19.set(app.state.e19.get() - Int(1)),  
                Int(1) 
            )
        ).Else(
            Int(0)  
        )
    )

@Subroutine(TealType.uint64)
def executeOneRule():
    return Or(
        start1(), 
        take_appointment(),
        xor1(),
        check_availability(),
        check_availability_resp(),
        xor2(),
        confirm_appointment(),
        and1(),
        check_certification(),
        check_temperature(),
        and2(),
        check_in(),
        check_in_resp(),
        xor3(),
        end1(),
        perform_xrays(),
        send_result(),
        end2()       
    )

@Subroutine(TealType.uint64)
def get_marking():
    return Add(
        app.state.e0.get(),
        app.state.e1.get(),
        app.state.e2.get(),
        app.state.e3.get(),
        app.state.e4.get(),
        app.state.e5.get(),
        app.state.e6.get(),
        app.state.e7.get(),
        app.state.e8.get(),
        app.state.e9.get(),
        app.state.e10.get(),
        app.state.e11.get(),
        app.state.e12.get(),
        app.state.e13.get(),
        app.state.e14.get(),
        app.state.e15.get(),
        app.state.e16.get(),
        app.state.e17.get(),
        app.state.e18.get(),
        app.state.e19.get()
    )

@app.external
def execute():
    return Seq(
        While(executeOneRule()).Do(
            If(app.state.enabled_messages.get() > Int(0)).Then(
            
            App.globalPut(Bytes("execution"),Bytes("waiting for Message")),
        ).Else(
            
            If(get_marking() > Int(0)).Then(
                App.globalPut(Bytes("execution"),Bytes("The choreography instance is DEADLOCKED"))
            ).Else(
                
                App.globalPut(Bytes("execution"),Bytes("The choreography instance is COMPLETE"))
            )
        ),
        
        Approve()  
    )
    )

if __name__ == "__main__":
    app.build().export()
