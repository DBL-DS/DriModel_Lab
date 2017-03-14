<?xml version="1.0" encoding="UTF-8"?>
<sc id="1" name="" frequency="1" steps="0" defaultIntergreenMatrix="0">
  <signaldisplays>
    <display id="1" name="Red" state="RED">
      <patterns>
        <pattern pattern="MINUS" color="#FF0000" isBold="true" />
      </patterns>
    </display>
    <display id="3" name="Green" state="GREEN">
      <patterns>
        <pattern pattern="FRAME" color="#00CC00" isBold="true" />
        <pattern pattern="SOLID" color="#00CC00" isBold="false" />
      </patterns>
    </display>
    <display id="4" name="Amber" state="AMBER">
      <patterns>
        <pattern pattern="FRAME" color="#CCCC00" isBold="true" />
        <pattern pattern="SLASH" color="#CCCC00" isBold="false" />
      </patterns>
    </display>
  </signaldisplays>
  <signalsequences>
    <signalsequence id="7" name="Red-Green-Amber">
      <state display="1" isFixedDuration="false" isClosed="true" defaultDuration="1000" />
      <state display="3" isFixedDuration="false" isClosed="false" defaultDuration="5000" />
      <state display="4" isFixedDuration="true" isClosed="true" defaultDuration="3000" />
    </signalsequence>
  </signalsequences>
  <sgs>
    <sg id="1" name="Signal group 1" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="2" name="Signal group 2" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="3" name="Signal group 3" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="4" name="Signal group 4" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="5" name="Signal group 5" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="6" name="Signal group 6" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="7" name="Signal group 7" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="8" name="Signal group 8" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="9" name="Signal group 9" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="10" name="Signal group 10" defaultSignalSequence="7" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="15000" />
        <defaultDuration display="4" duration="3000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
  </sgs>
  <dets />
  <messagePointPairs />
  <intergreenmatrices>
    <intergreenmatrix id="1" name="Intergreen matrix 1" />
  </intergreenmatrices>
  <progs>
    <prog id="1" cycletime="80000" switchpoint="0" offset="0" intergreens="0" fitness="0.000000" vehicleCount="0" name="Signal program 1">
      <sgs>
        <sg sg_id="1" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="1000" />
            <cmd display="1" begin="19000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="2" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="21000" />
            <cmd display="1" begin="39000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="3" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="1000" />
            <cmd display="1" begin="19000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="4" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="21000" />
            <cmd display="1" begin="39000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="5" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="41000" />
            <cmd display="1" begin="59000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="6" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="61000" />
            <cmd display="1" begin="79000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="7" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="41000" />
            <cmd display="1" begin="59000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="8" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="61000" />
            <cmd display="1" begin="79000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="9" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="1000" />
            <cmd display="1" begin="19000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="10" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="41000" />
            <cmd display="1" begin="59000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
      </sgs>
    </prog>
  </progs>
  <stages />
  <interstageProgs />
  <stageProgs />
  <dailyProgLists />
</sc>