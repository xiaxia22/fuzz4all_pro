# Interface Soundbank

**Source:** `java.desktop\javax\sound\midi\Soundbank.html`

### Class Description

```java
public interface
Soundbank
```

A

Soundbank

contains a set of

Instruments

that can be loaded
into a

Synthesizer

. Note that a Java Sound

Soundbank

is
different from a MIDI bank. MIDI permits up to 16383 banks, each containing
up to 128 instruments (also sometimes called programs, patches, or timbres).
However, a

Soundbank

can contain 16383 times 128 instruments, because
the instruments within a

Soundbank

are indexed by both a MIDI program
number and a MIDI bank number (via a

Patch

object). Thus, a

Soundbank

can be thought of as a collection of MIDI banks.

Soundbank

includes methods that return

String

objects
containing the sound bank's name, manufacturer, version number, and
description. The precise content and format of these strings is left to the
implementor.

Different synthesizers use a variety of synthesis techniques. A common one is
wavetable synthesis, in which a segment of recorded sound is played back,
often with looping and pitch change. The Downloadable Sound (DLS) format uses
segments of recorded sound, as does the Headspace Engine.

Soundbanks

and

Instruments

that are based on wavetable synthesis (or other uses
of stored sound recordings) should typically implement the

getResources()

method to provide access to these recorded segments.
This is optional, however; the method can return an zero-length array if the
synthesis technique doesn't use sampled sound (FM synthesis and physical
modeling are examples of such techniques), or if it does but the implementor
chooses not to make the samples accessible.

**See Also:** Synthesizer.getDefaultSoundbank()

,

Synthesizer.isSoundbankSupported(javax.sound.midi.Soundbank)

,

Synthesizer.loadInstruments(Soundbank, Patch[])

,

Patch

,

Instrument

,

SoundbankResource

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Obtains the name of the sound bank.

**Returns:**
- a

String

naming the sound bank

---

#### String
getVersion()

Obtains the version string for the sound bank.

**Returns:**
- a

String

that indicates the sound bank's version

---

#### String
getVendor()

Obtains a

string

naming the company that provides the sound bank.

**Returns:**
- the vendor string

---

#### String
getDescription()

Obtains a textual description of the sound bank, suitable for display.

**Returns:**
- a

String

that describes the sound bank

---

#### SoundbankResource
[] getResources()

Extracts a list of non-Instrument resources contained in the sound bank.

**Returns:**
- an array of resources, excluding instruments. If the sound bank
contains no resources (other than instruments), returns an array
of length 0.

---

#### Instrument
[] getInstruments()

Obtains a list of instruments contained in this sound bank.

**Returns:**
- an array of the

Instruments

in this

SoundBank

. If
the sound bank contains no instruments, returns an array of
length 0.

**See Also:**
- Synthesizer.getLoadedInstruments()

,

getInstrument(Patch)

---

#### Instrument
getInstrument​(
Patch
patch)

Obtains an

Instrument

from the given

Patch

.

**Parameters:**
- patch

- a

Patch

object specifying the bank index and
program change number

**Returns:**
- the requested instrument, or

null

if the sound bank
doesn't contain that instrument

**See Also:**
- getInstruments()

,

Synthesizer.loadInstruments(Soundbank, Patch[])

---

### Additional Sections

#### Interface Soundbank

```java
public interface
Soundbank
```

A

Soundbank

contains a set of

Instruments

that can be loaded
into a

Synthesizer

. Note that a Java Sound

Soundbank

is
different from a MIDI bank. MIDI permits up to 16383 banks, each containing
up to 128 instruments (also sometimes called programs, patches, or timbres).
However, a

Soundbank

can contain 16383 times 128 instruments, because
the instruments within a

Soundbank

are indexed by both a MIDI program
number and a MIDI bank number (via a

Patch

object). Thus, a

Soundbank

can be thought of as a collection of MIDI banks.

Soundbank

includes methods that return

String

objects
containing the sound bank's name, manufacturer, version number, and
description. The precise content and format of these strings is left to the
implementor.

Different synthesizers use a variety of synthesis techniques. A common one is
wavetable synthesis, in which a segment of recorded sound is played back,
often with looping and pitch change. The Downloadable Sound (DLS) format uses
segments of recorded sound, as does the Headspace Engine.

Soundbanks

and

Instruments

that are based on wavetable synthesis (or other uses
of stored sound recordings) should typically implement the

getResources()

method to provide access to these recorded segments.
This is optional, however; the method can return an zero-length array if the
synthesis technique doesn't use sampled sound (FM synthesis and physical
modeling are examples of such techniques), or if it does but the implementor
chooses not to make the samples accessible.

**See Also:** Synthesizer.getDefaultSoundbank()

,

Synthesizer.isSoundbankSupported(javax.sound.midi.Soundbank)

,

Synthesizer.loadInstruments(Soundbank, Patch[])

,

Patch

,

Instrument

,

SoundbankResource

public interface

Soundbank

A

Soundbank

contains a set of

Instruments

that can be loaded
into a

Synthesizer

. Note that a Java Sound

Soundbank

is
different from a MIDI bank. MIDI permits up to 16383 banks, each containing
up to 128 instruments (also sometimes called programs, patches, or timbres).
However, a

Soundbank

can contain 16383 times 128 instruments, because
the instruments within a

Soundbank

are indexed by both a MIDI program
number and a MIDI bank number (via a

Patch

object). Thus, a

Soundbank

can be thought of as a collection of MIDI banks.

Soundbank

includes methods that return

String

objects
containing the sound bank's name, manufacturer, version number, and
description. The precise content and format of these strings is left to the
implementor.

Different synthesizers use a variety of synthesis techniques. A common one is
wavetable synthesis, in which a segment of recorded sound is played back,
often with looping and pitch change. The Downloadable Sound (DLS) format uses
segments of recorded sound, as does the Headspace Engine.

Soundbanks

and

Instruments

that are based on wavetable synthesis (or other uses
of stored sound recordings) should typically implement the

getResources()

method to provide access to these recorded segments.
This is optional, however; the method can return an zero-length array if the
synthesis technique doesn't use sampled sound (FM synthesis and physical
modeling are examples of such techniques), or if it does but the implementor
chooses not to make the samples accessible.

Soundbank

includes methods that return

String

objects
containing the sound bank's name, manufacturer, version number, and
description. The precise content and format of these strings is left to the
implementor.

Different synthesizers use a variety of synthesis techniques. A common one is
wavetable synthesis, in which a segment of recorded sound is played back,
often with looping and pitch change. The Downloadable Sound (DLS) format uses
segments of recorded sound, as does the Headspace Engine.

Soundbanks

and

Instruments

that are based on wavetable synthesis (or other uses
of stored sound recordings) should typically implement the

getResources()

method to provide access to these recorded segments.
This is optional, however; the method can return an zero-length array if the
synthesis technique doesn't use sampled sound (FM synthesis and physical
modeling are examples of such techniques), or if it does but the implementor
chooses not to make the samples accessible.

Different synthesizers use a variety of synthesis techniques. A common one is
wavetable synthesis, in which a segment of recorded sound is played back,
often with looping and pitch change. The Downloadable Sound (DLS) format uses
segments of recorded sound, as does the Headspace Engine.

Soundbanks

and

Instruments

that are based on wavetable synthesis (or other uses
of stored sound recordings) should typically implement the

getResources()

method to provide access to these recorded segments.
This is optional, however; the method can return an zero-length array if the
synthesis technique doesn't use sampled sound (FM synthesis and physical
modeling are examples of such techniques), or if it does but the implementor
chooses not to make the samples accessible.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getDescription

()

Obtains a textual description of the sound bank, suitable for display.

Instrument

getInstrument

​(

Patch

patch)

Obtains an

Instrument

from the given

Patch

.

Instrument

[]

getInstruments

()

Obtains a list of instruments contained in this sound bank.

String

getName

()

Obtains the name of the sound bank.

SoundbankResource

[]

getResources

()

Extracts a list of non-Instrument resources contained in the sound bank.

String

getVendor

()

Obtains a

string

naming the company that provides the sound bank.

String

getVersion

()

Obtains the version string for the sound bank.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getDescription

()

Obtains a textual description of the sound bank, suitable for display.

Instrument

getInstrument

​(

Patch

patch)

Obtains an

Instrument

from the given

Patch

.

Instrument

[]

getInstruments

()

Obtains a list of instruments contained in this sound bank.

String

getName

()

Obtains the name of the sound bank.

SoundbankResource

[]

getResources

()

Extracts a list of non-Instrument resources contained in the sound bank.

String

getVendor

()

Obtains a

string

naming the company that provides the sound bank.

String

getVersion

()

Obtains the version string for the sound bank.

---

#### Method Summary

Obtains a textual description of the sound bank, suitable for display.

Obtains an

Instrument

from the given

Patch

.

Obtains a list of instruments contained in this sound bank.

Obtains the name of the sound bank.

Extracts a list of non-Instrument resources contained in the sound bank.

Obtains a

string

naming the company that provides the sound bank.

Obtains the version string for the sound bank.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Obtains the name of the sound bank.

**Returns:** a

String

naming the sound bank

- getVersion

```java
String
getVersion()
```

Obtains the version string for the sound bank.

**Returns:** a

String

that indicates the sound bank's version

- getVendor

```java
String
getVendor()
```

Obtains a

string

naming the company that provides the sound bank.

**Returns:** the vendor string

- getDescription

```java
String
getDescription()
```

Obtains a textual description of the sound bank, suitable for display.

**Returns:** a

String

that describes the sound bank

- getResources

```java
SoundbankResource
[] getResources()
```

Extracts a list of non-Instrument resources contained in the sound bank.

**Returns:** an array of resources, excluding instruments. If the sound bank
contains no resources (other than instruments), returns an array
of length 0.

- getInstruments

```java
Instrument
[] getInstruments()
```

Obtains a list of instruments contained in this sound bank.

**Returns:** an array of the

Instruments

in this

SoundBank

. If
the sound bank contains no instruments, returns an array of
length 0.
**See Also:** Synthesizer.getLoadedInstruments()

,

getInstrument(Patch)

- getInstrument

```java
Instrument
getInstrument​(
Patch
patch)
```

Obtains an

Instrument

from the given

Patch

.

**Parameters:** patch

- a

Patch

object specifying the bank index and
program change number
**Returns:** the requested instrument, or

null

if the sound bank
doesn't contain that instrument
**See Also:** getInstruments()

,

Synthesizer.loadInstruments(Soundbank, Patch[])

Method Detail

- getName

```java
String
getName()
```

Obtains the name of the sound bank.

**Returns:** a

String

naming the sound bank

- getVersion

```java
String
getVersion()
```

Obtains the version string for the sound bank.

**Returns:** a

String

that indicates the sound bank's version

- getVendor

```java
String
getVendor()
```

Obtains a

string

naming the company that provides the sound bank.

**Returns:** the vendor string

- getDescription

```java
String
getDescription()
```

Obtains a textual description of the sound bank, suitable for display.

**Returns:** a

String

that describes the sound bank

- getResources

```java
SoundbankResource
[] getResources()
```

Extracts a list of non-Instrument resources contained in the sound bank.

**Returns:** an array of resources, excluding instruments. If the sound bank
contains no resources (other than instruments), returns an array
of length 0.

- getInstruments

```java
Instrument
[] getInstruments()
```

Obtains a list of instruments contained in this sound bank.

**Returns:** an array of the

Instruments

in this

SoundBank

. If
the sound bank contains no instruments, returns an array of
length 0.
**See Also:** Synthesizer.getLoadedInstruments()

,

getInstrument(Patch)

- getInstrument

```java
Instrument
getInstrument​(
Patch
patch)
```

Obtains an

Instrument

from the given

Patch

.

**Parameters:** patch

- a

Patch

object specifying the bank index and
program change number
**Returns:** the requested instrument, or

null

if the sound bank
doesn't contain that instrument
**See Also:** getInstruments()

,

Synthesizer.loadInstruments(Soundbank, Patch[])

---

#### Method Detail

getName

```java
String
getName()
```

Obtains the name of the sound bank.

**Returns:** a

String

naming the sound bank

---

#### getName

String

getName()

Obtains the name of the sound bank.

getVersion

```java
String
getVersion()
```

Obtains the version string for the sound bank.

**Returns:** a

String

that indicates the sound bank's version

---

#### getVersion

String

getVersion()

Obtains the version string for the sound bank.

getVendor

```java
String
getVendor()
```

Obtains a

string

naming the company that provides the sound bank.

**Returns:** the vendor string

---

#### getVendor

String

getVendor()

Obtains a

string

naming the company that provides the sound bank.

getDescription

```java
String
getDescription()
```

Obtains a textual description of the sound bank, suitable for display.

**Returns:** a

String

that describes the sound bank

---

#### getDescription

String

getDescription()

Obtains a textual description of the sound bank, suitable for display.

getResources

```java
SoundbankResource
[] getResources()
```

Extracts a list of non-Instrument resources contained in the sound bank.

**Returns:** an array of resources, excluding instruments. If the sound bank
contains no resources (other than instruments), returns an array
of length 0.

---

#### getResources

SoundbankResource

[] getResources()

Extracts a list of non-Instrument resources contained in the sound bank.

getInstruments

```java
Instrument
[] getInstruments()
```

Obtains a list of instruments contained in this sound bank.

**Returns:** an array of the

Instruments

in this

SoundBank

. If
the sound bank contains no instruments, returns an array of
length 0.
**See Also:** Synthesizer.getLoadedInstruments()

,

getInstrument(Patch)

---

#### getInstruments

Instrument

[] getInstruments()

Obtains a list of instruments contained in this sound bank.

getInstrument

```java
Instrument
getInstrument​(
Patch
patch)
```

Obtains an

Instrument

from the given

Patch

.

**Parameters:** patch

- a

Patch

object specifying the bank index and
program change number
**Returns:** the requested instrument, or

null

if the sound bank
doesn't contain that instrument
**See Also:** getInstruments()

,

Synthesizer.loadInstruments(Soundbank, Patch[])

---

#### getInstrument

Instrument

getInstrument​(

Patch

patch)

Obtains an

Instrument

from the given

Patch

.

---

