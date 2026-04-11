# Class Patch

**Source:** `java.desktop\javax\sound\midi\Patch.html`

### Class Description

```java
public class
Patch

extends
Object
```

A

Patch

object represents a location, on a MIDI synthesizer, into
which a single instrument is stored (loaded). Every

Instrument

object
has its own

Patch

object that specifies the memory location into
which that instrument should be loaded. The location is specified abstractly
by a bank index and a program number (not by any scheme that directly refers
to a specific address or offset in RAM). This is a hierarchical indexing
scheme: MIDI provides for up to 16384 banks, each of which contains up to 128
program locations. For example, a minimal sort of synthesizer might have only
one bank of instruments, and only 32 instruments (programs) in that bank.

To select what instrument should play the notes on a particular MIDI channel,
two kinds of MIDI message are used that specify a patch location: a
bank-select command, and a program-change channel command. The Java Sound
equivalent is the

programChange(int, int)

method of

MidiChannel

.

**See Also:** Instrument

,

Instrument.getPatch()

,

MidiChannel.programChange(int, int)

,

Synthesizer.loadInstruments(Soundbank, Patch[])

,

Soundbank

,

Sequence.getPatchList()

---

### Field Details

*No entries found.*

### Constructor Details

#### public Patch​(int bank,
int program)

Constructs a new patch object from the specified bank and program
numbers.

**Parameters:**
- bank

- the bank index (in the range from 0 to 16383)
- program

- the program index (in the range from 0 to 127)

---

### Method Details

#### public int getBank()

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

**Returns:**
- the bank number, whose range is from 0 to 16383

**See Also:**
- MidiChannel.programChange(int, int)

---

#### public int getProgram()

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

**Returns:**
- the instrument's program number, whose range is from 0 to 127

**See Also:**
- MidiChannel.getProgram()

,

MidiChannel.programChange(int)

,

MidiChannel.programChange(int, int)

---

### Additional Sections

#### Class Patch

java.lang.Object

- javax.sound.midi.Patch

javax.sound.midi.Patch

```java
public class
Patch

extends
Object
```

A

Patch

object represents a location, on a MIDI synthesizer, into
which a single instrument is stored (loaded). Every

Instrument

object
has its own

Patch

object that specifies the memory location into
which that instrument should be loaded. The location is specified abstractly
by a bank index and a program number (not by any scheme that directly refers
to a specific address or offset in RAM). This is a hierarchical indexing
scheme: MIDI provides for up to 16384 banks, each of which contains up to 128
program locations. For example, a minimal sort of synthesizer might have only
one bank of instruments, and only 32 instruments (programs) in that bank.

To select what instrument should play the notes on a particular MIDI channel,
two kinds of MIDI message are used that specify a patch location: a
bank-select command, and a program-change channel command. The Java Sound
equivalent is the

programChange(int, int)

method of

MidiChannel

.

**See Also:** Instrument

,

Instrument.getPatch()

,

MidiChannel.programChange(int, int)

,

Synthesizer.loadInstruments(Soundbank, Patch[])

,

Soundbank

,

Sequence.getPatchList()

public class

Patch

extends

Object

A

Patch

object represents a location, on a MIDI synthesizer, into
which a single instrument is stored (loaded). Every

Instrument

object
has its own

Patch

object that specifies the memory location into
which that instrument should be loaded. The location is specified abstractly
by a bank index and a program number (not by any scheme that directly refers
to a specific address or offset in RAM). This is a hierarchical indexing
scheme: MIDI provides for up to 16384 banks, each of which contains up to 128
program locations. For example, a minimal sort of synthesizer might have only
one bank of instruments, and only 32 instruments (programs) in that bank.

To select what instrument should play the notes on a particular MIDI channel,
two kinds of MIDI message are used that specify a patch location: a
bank-select command, and a program-change channel command. The Java Sound
equivalent is the

programChange(int, int)

method of

MidiChannel

.

To select what instrument should play the notes on a particular MIDI channel,
two kinds of MIDI message are used that specify a patch location: a
bank-select command, and a program-change channel command. The Java Sound
equivalent is the

programChange(int, int)

method of

MidiChannel

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Patch

​(int bank,
int program)

Constructs a new patch object from the specified bank and program
numbers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBank

()

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

int

getProgram

()

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

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

Constructor

Description

Patch

​(int bank,
int program)

Constructs a new patch object from the specified bank and program
numbers.

---

#### Constructor Summary

Constructs a new patch object from the specified bank and program
numbers.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBank

()

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

int

getProgram

()

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

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

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

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

- Patch

```java
public Patch​(int bank,
int program)
```

Constructs a new patch object from the specified bank and program
numbers.

**Parameters:** bank

- the bank index (in the range from 0 to 16383)
**Parameters:** program

- the program index (in the range from 0 to 127)

============ METHOD DETAIL ==========

- Method Detail

- getBank

```java
public int getBank()
```

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

**Returns:** the bank number, whose range is from 0 to 16383
**See Also:** MidiChannel.programChange(int, int)

- getProgram

```java
public int getProgram()
```

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

**Returns:** the instrument's program number, whose range is from 0 to 127
**See Also:** MidiChannel.getProgram()

,

MidiChannel.programChange(int)

,

MidiChannel.programChange(int, int)

Constructor Detail

- Patch

```java
public Patch​(int bank,
int program)
```

Constructs a new patch object from the specified bank and program
numbers.

**Parameters:** bank

- the bank index (in the range from 0 to 16383)
**Parameters:** program

- the program index (in the range from 0 to 127)

---

#### Constructor Detail

Patch

```java
public Patch​(int bank,
int program)
```

Constructs a new patch object from the specified bank and program
numbers.

**Parameters:** bank

- the bank index (in the range from 0 to 16383)
**Parameters:** program

- the program index (in the range from 0 to 127)

---

#### Patch

public Patch​(int bank,
int program)

Constructs a new patch object from the specified bank and program
numbers.

Method Detail

- getBank

```java
public int getBank()
```

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

**Returns:** the bank number, whose range is from 0 to 16383
**See Also:** MidiChannel.programChange(int, int)

- getProgram

```java
public int getProgram()
```

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

**Returns:** the instrument's program number, whose range is from 0 to 127
**See Also:** MidiChannel.getProgram()

,

MidiChannel.programChange(int)

,

MidiChannel.programChange(int, int)

---

#### Method Detail

getBank

```java
public int getBank()
```

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

**Returns:** the bank number, whose range is from 0 to 16383
**See Also:** MidiChannel.programChange(int, int)

---

#### getBank

public int getBank()

Returns the number of the bank that contains the instrument whose
location this

Patch

specifies.

getProgram

```java
public int getProgram()
```

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

**Returns:** the instrument's program number, whose range is from 0 to 127
**See Also:** MidiChannel.getProgram()

,

MidiChannel.programChange(int)

,

MidiChannel.programChange(int, int)

---

#### getProgram

public int getProgram()

Returns the index, within a bank, of the instrument whose location this

Patch

specifies.

---

