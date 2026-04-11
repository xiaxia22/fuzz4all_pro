# Class Instrument

**Source:** `java.desktop\javax\sound\midi\Instrument.html`

### Class Description

```java
public abstract class
Instrument

extends
SoundbankResource
```

An instrument is a sound-synthesis algorithm with certain parameter settings,
usually designed to emulate a specific real-world musical instrument or to
achieve a specific sort of sound effect. Instruments are typically stored in
collections called soundbanks. Before the instrument can be used to play
notes, it must first be loaded onto a synthesizer, and then it must be
selected for use on one or more channels, via a program-change command. MIDI
notes that are subsequently received on those channels will be played using
the sound of the selected instrument.

**See Also:** Soundbank

,

Soundbank.getInstruments()

,

Patch

,

Synthesizer.loadInstrument(Instrument)

,

MidiChannel.programChange(int, int)

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Instrument​(
Soundbank
soundbank,

Patch
patch,

String
name,

Class
<?> dataClass)

Constructs a new MIDI instrument from the specified

Patch

. When a
subsequent request is made to load the instrument, the sound bank will
search its contents for this instrument's

Patch

, and the
instrument will be loaded into the synthesizer at the bank and program
location indicated by the

Patch

object.

**Parameters:**
- soundbank

- sound bank containing the instrument
- patch

- the patch of this instrument
- name

- the name of this instrument
- dataClass

- the class used to represent the sample's data

**See Also:**
- Synthesizer.loadInstrument(Instrument)

---

### Method Details

#### public
Patch
getPatch()

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

**Returns:**
- this instrument's patch

---

### Additional Sections

#### Class Instrument

java.lang.Object

- javax.sound.midi.SoundbankResource
- - javax.sound.midi.Instrument

javax.sound.midi.SoundbankResource

- javax.sound.midi.Instrument

javax.sound.midi.Instrument

```java
public abstract class
Instrument

extends
SoundbankResource
```

An instrument is a sound-synthesis algorithm with certain parameter settings,
usually designed to emulate a specific real-world musical instrument or to
achieve a specific sort of sound effect. Instruments are typically stored in
collections called soundbanks. Before the instrument can be used to play
notes, it must first be loaded onto a synthesizer, and then it must be
selected for use on one or more channels, via a program-change command. MIDI
notes that are subsequently received on those channels will be played using
the sound of the selected instrument.

**See Also:** Soundbank

,

Soundbank.getInstruments()

,

Patch

,

Synthesizer.loadInstrument(Instrument)

,

MidiChannel.programChange(int, int)

public abstract class

Instrument

extends

SoundbankResource

An instrument is a sound-synthesis algorithm with certain parameter settings,
usually designed to emulate a specific real-world musical instrument or to
achieve a specific sort of sound effect. Instruments are typically stored in
collections called soundbanks. Before the instrument can be used to play
notes, it must first be loaded onto a synthesizer, and then it must be
selected for use on one or more channels, via a program-change command. MIDI
notes that are subsequently received on those channels will be played using
the sound of the selected instrument.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Instrument

​(

Soundbank

soundbank,

Patch

patch,

String

name,

Class

<?> dataClass)

Constructs a new MIDI instrument from the specified

Patch

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Patch

getPatch

()

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

- Methods declared in class javax.sound.midi.

SoundbankResource

getData

,

getDataClass

,

getName

,

getSoundbank

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Instrument

​(

Soundbank

soundbank,

Patch

patch,

String

name,

Class

<?> dataClass)

Constructs a new MIDI instrument from the specified

Patch

.

---

#### Constructor Summary

Constructs a new MIDI instrument from the specified

Patch

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Patch

getPatch

()

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

- Methods declared in class javax.sound.midi.

SoundbankResource

getData

,

getDataClass

,

getName

,

getSoundbank

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

Methods declared in class javax.sound.midi.

SoundbankResource

getData

,

getDataClass

,

getName

,

getSoundbank

---

#### Methods declared in class javax.sound.midi. SoundbankResource

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Instrument

```java
protected Instrument​(
Soundbank
soundbank,

Patch
patch,

String
name,

Class
<?> dataClass)
```

Constructs a new MIDI instrument from the specified

Patch

. When a
subsequent request is made to load the instrument, the sound bank will
search its contents for this instrument's

Patch

, and the
instrument will be loaded into the synthesizer at the bank and program
location indicated by the

Patch

object.

**Parameters:** soundbank

- sound bank containing the instrument
**Parameters:** patch

- the patch of this instrument
**Parameters:** name

- the name of this instrument
**Parameters:** dataClass

- the class used to represent the sample's data
**See Also:** Synthesizer.loadInstrument(Instrument)

============ METHOD DETAIL ==========

- Method Detail

- getPatch

```java
public
Patch
getPatch()
```

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

**Returns:** this instrument's patch

Constructor Detail

- Instrument

```java
protected Instrument​(
Soundbank
soundbank,

Patch
patch,

String
name,

Class
<?> dataClass)
```

Constructs a new MIDI instrument from the specified

Patch

. When a
subsequent request is made to load the instrument, the sound bank will
search its contents for this instrument's

Patch

, and the
instrument will be loaded into the synthesizer at the bank and program
location indicated by the

Patch

object.

**Parameters:** soundbank

- sound bank containing the instrument
**Parameters:** patch

- the patch of this instrument
**Parameters:** name

- the name of this instrument
**Parameters:** dataClass

- the class used to represent the sample's data
**See Also:** Synthesizer.loadInstrument(Instrument)

---

#### Constructor Detail

Instrument

```java
protected Instrument​(
Soundbank
soundbank,

Patch
patch,

String
name,

Class
<?> dataClass)
```

Constructs a new MIDI instrument from the specified

Patch

. When a
subsequent request is made to load the instrument, the sound bank will
search its contents for this instrument's

Patch

, and the
instrument will be loaded into the synthesizer at the bank and program
location indicated by the

Patch

object.

**Parameters:** soundbank

- sound bank containing the instrument
**Parameters:** patch

- the patch of this instrument
**Parameters:** name

- the name of this instrument
**Parameters:** dataClass

- the class used to represent the sample's data
**See Also:** Synthesizer.loadInstrument(Instrument)

---

#### Instrument

protected Instrument​(

Soundbank

soundbank,

Patch

patch,

String

name,

Class

<?> dataClass)

Constructs a new MIDI instrument from the specified

Patch

. When a
subsequent request is made to load the instrument, the sound bank will
search its contents for this instrument's

Patch

, and the
instrument will be loaded into the synthesizer at the bank and program
location indicated by the

Patch

object.

Method Detail

- getPatch

```java
public
Patch
getPatch()
```

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

**Returns:** this instrument's patch

---

#### Method Detail

getPatch

```java
public
Patch
getPatch()
```

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

**Returns:** this instrument's patch

---

#### getPatch

public

Patch

getPatch()

Obtains the

Patch

object that indicates the bank and program
numbers where this instrument is to be stored in the synthesizer.

---

