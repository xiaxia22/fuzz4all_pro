# Class ExifTIFFTagSet

**Source:** `java.desktop\javax\imageio\plugins\tiff\ExifTIFFTagSet.html`

### Class Description

```java
public final class
ExifTIFFTagSet

extends
TIFFTagSet
```

A class representing the tags found in an Exif IFD. Exif is a
standard for annotating images used by most digital camera
manufacturers. The Exif specification may be found at

http://www.exif.org/Exif2-2.PDF

.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

**Since:** 9

---

### Field Details

#### public static final int TAG_GPS_INFO_IFD_POINTER

A tag pointing to a GPS info IFD (type LONG). This tag has
been superseded by

ExifParentTIFFTagSet.TAG_GPS_INFO_IFD_POINTER

.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_INTEROPERABILITY_IFD_POINTER

A tag pointing to an interoperability IFD (type LONG).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_EXIF_VERSION

A tag containing the Exif version number (type UNDEFINED, count =
4). Conformance to the Exif 2.1 standard is indicated using
the ASCII value "0210" (with no terminating NUL).

**See Also:**
- EXIF_VERSION_2_1

,

EXIF_VERSION_2_2

,

Constant Field Values

---

#### public static final
String
EXIF_VERSION_2_1

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1. The value equals the US-ASCII encoding of the byte array

{'0', '2', '1', '0'}

.

**See Also:**
- TAG_EXIF_VERSION

,

Constant Field Values

---

#### public static final
String
EXIF_VERSION_2_2

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2. The value equals the US-ASCII encoding of the byte array

{'0', '2', '2', '0'}

.

**See Also:**
- TAG_EXIF_VERSION

,

Constant Field Values

---

#### public static final int TAG_FLASHPIX_VERSION

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_COLOR_SPACE

A tag indicating the color space information (type SHORT). The
legal values are given by the

COLOR_SPACE_*

constants.

**See Also:**
- COLOR_SPACE_SRGB

,

COLOR_SPACE_UNCALIBRATED

,

Constant Field Values

---

#### public static final int COLOR_SPACE_SRGB

A value to be used with the "ColorSpace" tag.

**See Also:**
- TAG_COLOR_SPACE

,

Constant Field Values

---

#### public static final int COLOR_SPACE_UNCALIBRATED

A value to be used with the "ColorSpace" tag.

**See Also:**
- TAG_COLOR_SPACE

,

Constant Field Values

---

#### public static final int TAG_COMPONENTS_CONFIGURATION

A tag containing the components configuration information (type
UNDEFINED, count = 4).

**See Also:**
- COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

,

COMPONENTS_CONFIGURATION_Y

,

COMPONENTS_CONFIGURATION_CB

,

COMPONENTS_CONFIGURATION_CR

,

COMPONENTS_CONFIGURATION_R

,

COMPONENTS_CONFIGURATION_G

,

COMPONENTS_CONFIGURATION_B

,

Constant Field Values

---

#### public static final int COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

A value to be used with the "ComponentsConfiguration" tag.

**See Also:**
- TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### public static final int COMPONENTS_CONFIGURATION_Y

A value to be used with the "ComponentsConfiguration" tag.

**See Also:**
- TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### public static final int COMPONENTS_CONFIGURATION_CB

A value to be used with the "ComponentsConfiguration" tag.

**See Also:**
- TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### public static final int COMPONENTS_CONFIGURATION_CR

A value to be used with the "ComponentsConfiguration" tag.

**See Also:**
- TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### public static final int COMPONENTS_CONFIGURATION_R

A value to be used with the "ComponentsConfiguration" tag.

**See Also:**
- TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### public static final int COMPONENTS_CONFIGURATION_G

A value to be used with the "ComponentsConfiguration" tag.

**See Also:**
- TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### public static final int COMPONENTS_CONFIGURATION_B

A value to be used with the "ComponentsConfiguration" tag.

**See Also:**
- TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### public static final int TAG_COMPRESSED_BITS_PER_PIXEL

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_PIXEL_X_DIMENSION

A tag indicating the pixel X dimension (type SHORT or LONG).
This value records the valid width of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_PIXEL_Y_DIMENSION

A tag indicating the pixel Y dimension (type SHORT or LONG).
This value records the valid height of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MAKER_NOTE

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MARKER_NOTE

A tag indicating a manufacturer-defined marker note (type UNDEFINED).
This tag has been superseded by

TAG_MAKER_NOTE

.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_USER_COMMENT

A tag indicating a user comment (type UNDEFINED). The first 8
bytes are used to specify the character encoding.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_RELATED_SOUND_FILE

A tag indicating the name of a related sound file (type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_DATE_TIME_ORIGINAL

A tag indicating the date and time when the original image was
generated (type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_DATE_TIME_DIGITIZED

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SUB_SEC_TIME

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SUB_SEC_TIME_ORIGINAL

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SUB_SEC_TIME_DIGITIZED

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_EXPOSURE_TIME

A tag indicating the exposure time, in seconds (type RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_F_NUMBER

A tag indicating the F number (type RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_EXPOSURE_PROGRAM

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

**See Also:**
- EXPOSURE_PROGRAM_NOT_DEFINED

,

EXPOSURE_PROGRAM_MANUAL

,

EXPOSURE_PROGRAM_NORMAL_PROGRAM

,

EXPOSURE_PROGRAM_APERTURE_PRIORITY

,

EXPOSURE_PROGRAM_SHUTTER_PRIORITY

,

EXPOSURE_PROGRAM_CREATIVE_PROGRAM

,

EXPOSURE_PROGRAM_ACTION_PROGRAM

,

EXPOSURE_PROGRAM_PORTRAIT_MODE

,

EXPOSURE_PROGRAM_LANDSCAPE_MODE

,

EXPOSURE_PROGRAM_MAX_RESERVED

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_NOT_DEFINED

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_MANUAL

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_NORMAL_PROGRAM

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_APERTURE_PRIORITY

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_SHUTTER_PRIORITY

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_CREATIVE_PROGRAM

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_ACTION_PROGRAM

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_PORTRAIT_MODE

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_LANDSCAPE_MODE

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int EXPOSURE_PROGRAM_MAX_RESERVED

A value to be used with the "ExposureProgram" tag.

**See Also:**
- TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### public static final int TAG_SPECTRAL_SENSITIVITY

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII). The tag value is an ASCII string
compatible with the ASTM standard.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_ISO_SPEED_RATINGS

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_OECF

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED). OECF is
the relationship between the camera optical input and the image
values.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SHUTTER_SPEED_VALUE

A tag indicating the shutter speed (type SRATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_APERTURE_VALUE

A tag indicating the lens aperture (type RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_BRIGHTNESS_VALUE

A tag indicating the value of brightness (type SRATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_EXPOSURE_BIAS_VALUE

A tag indicating the exposure bias (type SRATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_MAX_APERTURE_VALUE

A tag indicating the smallest F number of the lens (type
RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SUBJECT_DISTANCE

A tag indicating the distance to the subject, in meters (type
RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_METERING_MODE

A tag indicating the metering mode (type SHORT).

**See Also:**
- METERING_MODE_UNKNOWN

,

METERING_MODE_AVERAGE

,

METERING_MODE_CENTER_WEIGHTED_AVERAGE

,

METERING_MODE_SPOT

,

METERING_MODE_MULTI_SPOT

,

METERING_MODE_PATTERN

,

METERING_MODE_PARTIAL

,

METERING_MODE_MIN_RESERVED

,

METERING_MODE_MAX_RESERVED

,

METERING_MODE_OTHER

,

Constant Field Values

---

#### public static final int METERING_MODE_UNKNOWN

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_AVERAGE

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_CENTER_WEIGHTED_AVERAGE

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_SPOT

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_MULTI_SPOT

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_PATTERN

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_PARTIAL

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_MIN_RESERVED

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_MAX_RESERVED

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int METERING_MODE_OTHER

A value to be used with the "MeteringMode" tag.

**See Also:**
- TAG_METERING_MODE

,

Constant Field Values

---

#### public static final int TAG_LIGHT_SOURCE

A tag indicatingthe kind of light source (type SHORT).

**See Also:**
- LIGHT_SOURCE_UNKNOWN

,

LIGHT_SOURCE_DAYLIGHT

,

LIGHT_SOURCE_FLUORESCENT

,

LIGHT_SOURCE_TUNGSTEN

,

LIGHT_SOURCE_STANDARD_LIGHT_A

,

LIGHT_SOURCE_STANDARD_LIGHT_B

,

LIGHT_SOURCE_STANDARD_LIGHT_C

,

LIGHT_SOURCE_D55

,

LIGHT_SOURCE_D65

,

LIGHT_SOURCE_D75

,

LIGHT_SOURCE_OTHER

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_UNKNOWN

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_DAYLIGHT

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_FLUORESCENT

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_TUNGSTEN

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_FLASH

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_FINE_WEATHER

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_CLOUDY_WEATHER

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_SHADE

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_STANDARD_LIGHT_A

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_STANDARD_LIGHT_B

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_STANDARD_LIGHT_C

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_D55

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_D65

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_D75

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_D50

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int LIGHT_SOURCE_OTHER

A value to be used with the "LightSource" tag.

**See Also:**
- TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### public static final int TAG_FLASH

A tag indicating the flash firing status and flash return
status (type SHORT).

**See Also:**
- FLASH_DID_NOT_FIRE

,

FLASH_FIRED

,

FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

,

FLASH_STROBE_RETURN_LIGHT_DETECTED

,

Constant Field Values

---

#### public static final int FLASH_DID_NOT_FIRE

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_FIRED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_STROBE_RETURN_LIGHT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_FIRED

A mask to be used with the "Flash" tag, indicating that the
flash fired.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_RETURN_NOT_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_RETURN_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_MODE_FLASH_FIRING

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_MODE_FLASH_SUPPRESSION

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_MODE_AUTO

A mask to be used with the "Flash" tag, indicating auto mode.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_FUNCTION_NOT_PRESENT

A mask to be used with the "Flash" tag, indicating no flash function
present.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int FLASH_MASK_RED_EYE_REDUCTION

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

**See Also:**
- TAG_FLASH

,

Constant Field Values

---

#### public static final int TAG_FOCAL_LENGTH

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SUBJECT_AREA

A tag indicating the location and area of the main subject in
the overall scene.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FLASH_ENERGY

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SPATIAL_FREQUENCY_RESPONSE

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FOCAL_PLANE_X_RESOLUTION

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FOCAL_PLANE_Y_RESOLUTION

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FOCAL_PLANE_RESOLUTION_UNIT

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

**See Also:**
- FOCAL_PLANE_RESOLUTION_UNIT_NONE

,

FOCAL_PLANE_RESOLUTION_UNIT_INCH

,

FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

---

#### public static final int FOCAL_PLANE_RESOLUTION_UNIT_NONE

A value to be used with the "FocalPlaneResolutionUnit" tag.

**See Also:**
- TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

---

#### public static final int FOCAL_PLANE_RESOLUTION_UNIT_INCH

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:**
- TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

---

#### public static final int FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:**
- TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

---

#### public static final int TAG_SUBJECT_LOCATION

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_EXPOSURE_INDEX

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SENSING_METHOD

A tag indicating the sensor type on the camera or input device
(type SHORT).

**See Also:**
- SENSING_METHOD_NOT_DEFINED

,

SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

,

SENSING_METHOD_TRILINEAR_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

,

Constant Field Values

---

#### public static final int SENSING_METHOD_NOT_DEFINED

A value to be used with the "SensingMethod" tag.

**See Also:**
- TAG_SENSING_METHOD

,

Constant Field Values

---

#### public static final int SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

**See Also:**
- TAG_SENSING_METHOD

,

Constant Field Values

---

#### public static final int SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

**See Also:**
- TAG_SENSING_METHOD

,

Constant Field Values

---

#### public static final int SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

**See Also:**
- TAG_SENSING_METHOD

,

Constant Field Values

---

#### public static final int SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

**See Also:**
- TAG_SENSING_METHOD

,

Constant Field Values

---

#### public static final int SENSING_METHOD_TRILINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

**See Also:**
- TAG_SENSING_METHOD

,

Constant Field Values

---

#### public static final int SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

**See Also:**
- TAG_SENSING_METHOD

,

Constant Field Values

---

#### public static final int TAG_FILE_SOURCE

A tag indicating the image source (type UNDEFINED).

**See Also:**
- FILE_SOURCE_DSC

,

Constant Field Values

---

#### public static final int FILE_SOURCE_DSC

A value to be used with the "FileSource" tag.

**See Also:**
- TAG_FILE_SOURCE

,

Constant Field Values

---

#### public static final int TAG_SCENE_TYPE

A tag indicating the type of scene (type UNDEFINED).

**See Also:**
- SCENE_TYPE_DSC

,

Constant Field Values

---

#### public static final int SCENE_TYPE_DSC

A value to be used with the "SceneType" tag.

**See Also:**
- TAG_SCENE_TYPE

,

Constant Field Values

---

#### public static final int TAG_CFA_PATTERN

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_CUSTOM_RENDERED

A tag indicating the use of special processing on image data,
such as rendering geared to output.

**See Also:**
- Constant Field Values

---

#### public static final int CUSTOM_RENDERED_NORMAL

A value to be used with the "CustomRendered" tag.

**See Also:**
- TAG_CUSTOM_RENDERED

,

Constant Field Values

---

#### public static final int CUSTOM_RENDERED_CUSTOM

A value to be used with the "CustomRendered" tag.

**See Also:**
- TAG_CUSTOM_RENDERED

,

Constant Field Values

---

#### public static final int TAG_EXPOSURE_MODE

A tag indicating the exposure mode set when the image was shot.

**See Also:**
- Constant Field Values

---

#### public static final int EXPOSURE_MODE_AUTO_EXPOSURE

A value to be used with the "ExposureMode" tag.

**See Also:**
- TAG_EXPOSURE_MODE

,

Constant Field Values

---

#### public static final int EXPOSURE_MODE_MANUAL_EXPOSURE

A value to be used with the "ExposureMode" tag.

**See Also:**
- TAG_EXPOSURE_MODE

,

Constant Field Values

---

#### public static final int EXPOSURE_MODE_AUTO_BRACKET

A value to be used with the "ExposureMode" tag.

**See Also:**
- TAG_EXPOSURE_MODE

,

Constant Field Values

---

#### public static final int TAG_WHITE_BALANCE

A tag indicating the white balance mode set when the image was shot.

**See Also:**
- Constant Field Values

---

#### public static final int WHITE_BALANCE_AUTO

A value to be used with the "WhiteBalance" tag.

**See Also:**
- TAG_WHITE_BALANCE

,

Constant Field Values

---

#### public static final int WHITE_BALANCE_MANUAL

A value to be used with the "WhiteBalance" tag.

**See Also:**
- TAG_WHITE_BALANCE

,

Constant Field Values

---

#### public static final int TAG_DIGITAL_ZOOM_RATIO

A tag indicating the digital zoom ratio when the image was shot.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_FOCAL_LENGTH_IN_35MM_FILM

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SCENE_CAPTURE_TYPE

A tag indicating the type of scene that was shot.

**See Also:**
- Constant Field Values

---

#### public static final int SCENE_CAPTURE_TYPE_STANDARD

A value to be used with the "SceneCaptureType" tag.

**See Also:**
- TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### public static final int SCENE_CAPTURE_TYPE_LANDSCAPE

A value to be used with the "SceneCaptureType" tag.

**See Also:**
- TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### public static final int SCENE_CAPTURE_TYPE_PORTRAIT

A value to be used with the "SceneCaptureType" tag.

**See Also:**
- TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### public static final int SCENE_CAPTURE_TYPE_NIGHT_SCENE

A value to be used with the "SceneCaptureType" tag.

**See Also:**
- TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### public static final int TAG_GAIN_CONTROL

A tag indicating the degree of overall image gain adjustment.

**See Also:**
- Constant Field Values

---

#### public static final int GAIN_CONTROL_NONE

A value to be used with the "GainControl" tag.

**See Also:**
- TAG_GAIN_CONTROL

,

Constant Field Values

---

#### public static final int GAIN_CONTROL_LOW_GAIN_UP

A value to be used with the "GainControl" tag.

**See Also:**
- TAG_GAIN_CONTROL

,

Constant Field Values

---

#### public static final int GAIN_CONTROL_HIGH_GAIN_UP

A value to be used with the "GainControl" tag.

**See Also:**
- TAG_GAIN_CONTROL

,

Constant Field Values

---

#### public static final int GAIN_CONTROL_LOW_GAIN_DOWN

A value to be used with the "GainControl" tag.

**See Also:**
- TAG_GAIN_CONTROL

,

Constant Field Values

---

#### public static final int GAIN_CONTROL_HIGH_GAIN_DOWN

A value to be used with the "GainControl" tag.

**See Also:**
- TAG_GAIN_CONTROL

,

Constant Field Values

---

#### public static final int TAG_CONTRAST

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

**See Also:**
- Constant Field Values

---

#### public static final int CONTRAST_NORMAL

A value to be used with the "Contrast" tag.

**See Also:**
- TAG_CONTRAST

,

Constant Field Values

---

#### public static final int CONTRAST_SOFT

A value to be used with the "Contrast" tag.

**See Also:**
- TAG_CONTRAST

,

Constant Field Values

---

#### public static final int CONTRAST_HARD

A value to be used with the "Contrast" tag.

**See Also:**
- TAG_CONTRAST

,

Constant Field Values

---

#### public static final int TAG_SATURATION

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

**See Also:**
- Constant Field Values

---

#### public static final int SATURATION_NORMAL

A value to be used with the "Saturation" tag.

**See Also:**
- TAG_SATURATION

,

Constant Field Values

---

#### public static final int SATURATION_LOW

A value to be used with the "Saturation" tag.

**See Also:**
- TAG_SATURATION

,

Constant Field Values

---

#### public static final int SATURATION_HIGH

A value to be used with the "Saturation" tag.

**See Also:**
- TAG_SATURATION

,

Constant Field Values

---

#### public static final int TAG_SHARPNESS

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

**See Also:**
- Constant Field Values

---

#### public static final int SHARPNESS_NORMAL

A value to be used with the "Sharpness" tag.

**See Also:**
- TAG_SHARPNESS

,

Constant Field Values

---

#### public static final int SHARPNESS_SOFT

A value to be used with the "Sharpness" tag.

**See Also:**
- TAG_SHARPNESS

,

Constant Field Values

---

#### public static final int SHARPNESS_HARD

A value to be used with the "Sharpness" tag.

**See Also:**
- TAG_SHARPNESS

,

Constant Field Values

---

#### public static final int TAG_DEVICE_SETTING_DESCRIPTION

A tag indicating information on the picture-taking conditions
of a particular camera model.

**See Also:**
- Constant Field Values

---

#### public static final int TAG_SUBJECT_DISTANCE_RANGE

A tag indicating the distance to the subject.

**See Also:**
- Constant Field Values

---

#### public static final int SUBJECT_DISTANCE_RANGE_UNKNOWN

A value to be used with the "SubjectDistanceRange" tag.

**See Also:**
- TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### public static final int SUBJECT_DISTANCE_RANGE_MACRO

A value to be used with the "SubjectDistanceRange" tag.

**See Also:**
- TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### public static final int SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

A value to be used with the "SubjectDistanceRange" tag.

**See Also:**
- TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### public static final int SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

A value to be used with the "SubjectDistanceRange" tag.

**See Also:**
- TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### public static final int TAG_IMAGE_UNIQUE_ID

A tag indicating an identifier assigned uniquely to each image.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
ExifTIFFTagSet
getInstance()

Returns a shared instance of an

ExifTIFFTagSet

.

**Returns:**
- an

ExifTIFFTagSet

instance.

---

### Additional Sections

#### Class ExifTIFFTagSet

java.lang.Object

- javax.imageio.plugins.tiff.TIFFTagSet
- - javax.imageio.plugins.tiff.ExifTIFFTagSet

javax.imageio.plugins.tiff.TIFFTagSet

- javax.imageio.plugins.tiff.ExifTIFFTagSet

javax.imageio.plugins.tiff.ExifTIFFTagSet

```java
public final class
ExifTIFFTagSet

extends
TIFFTagSet
```

A class representing the tags found in an Exif IFD. Exif is a
standard for annotating images used by most digital camera
manufacturers. The Exif specification may be found at

http://www.exif.org/Exif2-2.PDF

.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

**Since:** 9

public final class

ExifTIFFTagSet

extends

TIFFTagSet

A class representing the tags found in an Exif IFD. Exif is a
standard for annotating images used by most digital camera
manufacturers. The Exif specification may be found at

http://www.exif.org/Exif2-2.PDF

.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

COLOR_SPACE_SRGB

A value to be used with the "ColorSpace" tag.

static int

COLOR_SPACE_UNCALIBRATED

A value to be used with the "ColorSpace" tag.

static int

COMPONENTS_CONFIGURATION_B

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_CB

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_CR

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_G

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_R

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_Y

A value to be used with the "ComponentsConfiguration" tag.

static int

CONTRAST_HARD

A value to be used with the "Contrast" tag.

static int

CONTRAST_NORMAL

A value to be used with the "Contrast" tag.

static int

CONTRAST_SOFT

A value to be used with the "Contrast" tag.

static int

CUSTOM_RENDERED_CUSTOM

A value to be used with the "CustomRendered" tag.

static int

CUSTOM_RENDERED_NORMAL

A value to be used with the "CustomRendered" tag.

static

String

EXIF_VERSION_2_1

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1.

static

String

EXIF_VERSION_2_2

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2.

static int

EXPOSURE_MODE_AUTO_BRACKET

A value to be used with the "ExposureMode" tag.

static int

EXPOSURE_MODE_AUTO_EXPOSURE

A value to be used with the "ExposureMode" tag.

static int

EXPOSURE_MODE_MANUAL_EXPOSURE

A value to be used with the "ExposureMode" tag.

static int

EXPOSURE_PROGRAM_ACTION_PROGRAM

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_APERTURE_PRIORITY

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_CREATIVE_PROGRAM

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_LANDSCAPE_MODE

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_MANUAL

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_MAX_RESERVED

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_NORMAL_PROGRAM

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_NOT_DEFINED

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_PORTRAIT_MODE

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_SHUTTER_PRIORITY

A value to be used with the "ExposureProgram" tag.

static int

FILE_SOURCE_DSC

A value to be used with the "FileSource" tag.

static int

FLASH_DID_NOT_FIRE

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

static int

FLASH_FIRED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

static int

FLASH_MASK_FIRED

A mask to be used with the "Flash" tag, indicating that the
flash fired.

static int

FLASH_MASK_FUNCTION_NOT_PRESENT

A mask to be used with the "Flash" tag, indicating no flash function
present.

static int

FLASH_MASK_MODE_AUTO

A mask to be used with the "Flash" tag, indicating auto mode.

static int

FLASH_MASK_MODE_FLASH_FIRING

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

static int

FLASH_MASK_MODE_FLASH_SUPPRESSION

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

static int

FLASH_MASK_RED_EYE_REDUCTION

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

static int

FLASH_MASK_RETURN_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

static int

FLASH_MASK_RETURN_NOT_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

static int

FLASH_STROBE_RETURN_LIGHT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

static int

FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

static int

FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

A value to be used with the "FocalPlaneXResolution" tag.

static int

FOCAL_PLANE_RESOLUTION_UNIT_INCH

A value to be used with the "FocalPlaneXResolution" tag.

static int

FOCAL_PLANE_RESOLUTION_UNIT_NONE

A value to be used with the "FocalPlaneResolutionUnit" tag.

static int

GAIN_CONTROL_HIGH_GAIN_DOWN

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_HIGH_GAIN_UP

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_LOW_GAIN_DOWN

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_LOW_GAIN_UP

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_NONE

A value to be used with the "GainControl" tag.

static int

LIGHT_SOURCE_CLOUDY_WEATHER

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D50

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D55

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D65

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D75

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_DAYLIGHT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_FINE_WEATHER

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_FLASH

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_OTHER

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_SHADE

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_STANDARD_LIGHT_A

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_STANDARD_LIGHT_B

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_STANDARD_LIGHT_C

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_TUNGSTEN

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_UNKNOWN

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

METERING_MODE_AVERAGE

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_CENTER_WEIGHTED_AVERAGE

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_MAX_RESERVED

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_MIN_RESERVED

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_MULTI_SPOT

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_OTHER

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_PARTIAL

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_PATTERN

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_SPOT

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_UNKNOWN

A value to be used with the "MeteringMode" tag.

static int

SATURATION_HIGH

A value to be used with the "Saturation" tag.

static int

SATURATION_LOW

A value to be used with the "Saturation" tag.

static int

SATURATION_NORMAL

A value to be used with the "Saturation" tag.

static int

SCENE_CAPTURE_TYPE_LANDSCAPE

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_CAPTURE_TYPE_NIGHT_SCENE

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_CAPTURE_TYPE_PORTRAIT

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_CAPTURE_TYPE_STANDARD

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_TYPE_DSC

A value to be used with the "SceneType" tag.

static int

SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_NOT_DEFINED

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_TRILINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SHARPNESS_HARD

A value to be used with the "Sharpness" tag.

static int

SHARPNESS_NORMAL

A value to be used with the "Sharpness" tag.

static int

SHARPNESS_SOFT

A value to be used with the "Sharpness" tag.

static int

SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

A value to be used with the "SubjectDistanceRange" tag.

static int

SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

A value to be used with the "SubjectDistanceRange" tag.

static int

SUBJECT_DISTANCE_RANGE_MACRO

A value to be used with the "SubjectDistanceRange" tag.

static int

SUBJECT_DISTANCE_RANGE_UNKNOWN

A value to be used with the "SubjectDistanceRange" tag.

static int

TAG_APERTURE_VALUE

A tag indicating the lens aperture (type RATIONAL).

static int

TAG_BRIGHTNESS_VALUE

A tag indicating the value of brightness (type SRATIONAL).

static int

TAG_CFA_PATTERN

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

static int

TAG_COLOR_SPACE

A tag indicating the color space information (type SHORT).

static int

TAG_COMPONENTS_CONFIGURATION

A tag containing the components configuration information (type
UNDEFINED, count = 4).

static int

TAG_COMPRESSED_BITS_PER_PIXEL

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

static int

TAG_CONTRAST

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

static int

TAG_CUSTOM_RENDERED

A tag indicating the use of special processing on image data,
such as rendering geared to output.

static int

TAG_DATE_TIME_DIGITIZED

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

static int

TAG_DATE_TIME_ORIGINAL

A tag indicating the date and time when the original image was
generated (type ASCII).

static int

TAG_DEVICE_SETTING_DESCRIPTION

A tag indicating information on the picture-taking conditions
of a particular camera model.

static int

TAG_DIGITAL_ZOOM_RATIO

A tag indicating the digital zoom ratio when the image was shot.

static int

TAG_EXIF_VERSION

A tag containing the Exif version number (type UNDEFINED, count =
4).

static int

TAG_EXPOSURE_BIAS_VALUE

A tag indicating the exposure bias (type SRATIONAL).

static int

TAG_EXPOSURE_INDEX

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

static int

TAG_EXPOSURE_MODE

A tag indicating the exposure mode set when the image was shot.

static int

TAG_EXPOSURE_PROGRAM

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

static int

TAG_EXPOSURE_TIME

A tag indicating the exposure time, in seconds (type RATIONAL).

static int

TAG_F_NUMBER

A tag indicating the F number (type RATIONAL).

static int

TAG_FILE_SOURCE

A tag indicating the image source (type UNDEFINED).

static int

TAG_FLASH

A tag indicating the flash firing status and flash return
status (type SHORT).

static int

TAG_FLASH_ENERGY

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

static int

TAG_FLASHPIX_VERSION

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

static int

TAG_FOCAL_LENGTH

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

static int

TAG_FOCAL_LENGTH_IN_35MM_FILM

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

static int

TAG_FOCAL_PLANE_RESOLUTION_UNIT

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

static int

TAG_FOCAL_PLANE_X_RESOLUTION

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

static int

TAG_FOCAL_PLANE_Y_RESOLUTION

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

static int

TAG_GAIN_CONTROL

A tag indicating the degree of overall image gain adjustment.

static int

TAG_GPS_INFO_IFD_POINTER

A tag pointing to a GPS info IFD (type LONG).

static int

TAG_IMAGE_UNIQUE_ID

A tag indicating an identifier assigned uniquely to each image.

static int

TAG_INTEROPERABILITY_IFD_POINTER

A tag pointing to an interoperability IFD (type LONG).

static int

TAG_ISO_SPEED_RATINGS

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

static int

TAG_LIGHT_SOURCE

A tag indicatingthe kind of light source (type SHORT).

static int

TAG_MAKER_NOTE

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

static int

TAG_MARKER_NOTE

A tag indicating a manufacturer-defined marker note (type UNDEFINED).

static int

TAG_MAX_APERTURE_VALUE

A tag indicating the smallest F number of the lens (type
RATIONAL).

static int

TAG_METERING_MODE

A tag indicating the metering mode (type SHORT).

static int

TAG_OECF

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED).

static int

TAG_PIXEL_X_DIMENSION

A tag indicating the pixel X dimension (type SHORT or LONG).

static int

TAG_PIXEL_Y_DIMENSION

A tag indicating the pixel Y dimension (type SHORT or LONG).

static int

TAG_RELATED_SOUND_FILE

A tag indicating the name of a related sound file (type ASCII).

static int

TAG_SATURATION

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

static int

TAG_SCENE_CAPTURE_TYPE

A tag indicating the type of scene that was shot.

static int

TAG_SCENE_TYPE

A tag indicating the type of scene (type UNDEFINED).

static int

TAG_SENSING_METHOD

A tag indicating the sensor type on the camera or input device
(type SHORT).

static int

TAG_SHARPNESS

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

static int

TAG_SHUTTER_SPEED_VALUE

A tag indicating the shutter speed (type SRATIONAL).

static int

TAG_SPATIAL_FREQUENCY_RESPONSE

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

static int

TAG_SPECTRAL_SENSITIVITY

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII).

static int

TAG_SUB_SEC_TIME

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

static int

TAG_SUB_SEC_TIME_DIGITIZED

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

static int

TAG_SUB_SEC_TIME_ORIGINAL

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

static int

TAG_SUBJECT_AREA

A tag indicating the location and area of the main subject in
the overall scene.

static int

TAG_SUBJECT_DISTANCE

A tag indicating the distance to the subject, in meters (type
RATIONAL).

static int

TAG_SUBJECT_DISTANCE_RANGE

A tag indicating the distance to the subject.

static int

TAG_SUBJECT_LOCATION

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

static int

TAG_USER_COMMENT

A tag indicating a user comment (type UNDEFINED).

static int

TAG_WHITE_BALANCE

A tag indicating the white balance mode set when the image was shot.

static int

WHITE_BALANCE_AUTO

A value to be used with the "WhiteBalance" tag.

static int

WHITE_BALANCE_MANUAL

A value to be used with the "WhiteBalance" tag.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ExifTIFFTagSet

getInstance

()

Returns a shared instance of an

ExifTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

COLOR_SPACE_SRGB

A value to be used with the "ColorSpace" tag.

static int

COLOR_SPACE_UNCALIBRATED

A value to be used with the "ColorSpace" tag.

static int

COMPONENTS_CONFIGURATION_B

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_CB

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_CR

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_G

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_R

A value to be used with the "ComponentsConfiguration" tag.

static int

COMPONENTS_CONFIGURATION_Y

A value to be used with the "ComponentsConfiguration" tag.

static int

CONTRAST_HARD

A value to be used with the "Contrast" tag.

static int

CONTRAST_NORMAL

A value to be used with the "Contrast" tag.

static int

CONTRAST_SOFT

A value to be used with the "Contrast" tag.

static int

CUSTOM_RENDERED_CUSTOM

A value to be used with the "CustomRendered" tag.

static int

CUSTOM_RENDERED_NORMAL

A value to be used with the "CustomRendered" tag.

static

String

EXIF_VERSION_2_1

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1.

static

String

EXIF_VERSION_2_2

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2.

static int

EXPOSURE_MODE_AUTO_BRACKET

A value to be used with the "ExposureMode" tag.

static int

EXPOSURE_MODE_AUTO_EXPOSURE

A value to be used with the "ExposureMode" tag.

static int

EXPOSURE_MODE_MANUAL_EXPOSURE

A value to be used with the "ExposureMode" tag.

static int

EXPOSURE_PROGRAM_ACTION_PROGRAM

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_APERTURE_PRIORITY

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_CREATIVE_PROGRAM

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_LANDSCAPE_MODE

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_MANUAL

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_MAX_RESERVED

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_NORMAL_PROGRAM

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_NOT_DEFINED

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_PORTRAIT_MODE

A value to be used with the "ExposureProgram" tag.

static int

EXPOSURE_PROGRAM_SHUTTER_PRIORITY

A value to be used with the "ExposureProgram" tag.

static int

FILE_SOURCE_DSC

A value to be used with the "FileSource" tag.

static int

FLASH_DID_NOT_FIRE

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

static int

FLASH_FIRED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

static int

FLASH_MASK_FIRED

A mask to be used with the "Flash" tag, indicating that the
flash fired.

static int

FLASH_MASK_FUNCTION_NOT_PRESENT

A mask to be used with the "Flash" tag, indicating no flash function
present.

static int

FLASH_MASK_MODE_AUTO

A mask to be used with the "Flash" tag, indicating auto mode.

static int

FLASH_MASK_MODE_FLASH_FIRING

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

static int

FLASH_MASK_MODE_FLASH_SUPPRESSION

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

static int

FLASH_MASK_RED_EYE_REDUCTION

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

static int

FLASH_MASK_RETURN_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

static int

FLASH_MASK_RETURN_NOT_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

static int

FLASH_STROBE_RETURN_LIGHT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

static int

FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

static int

FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

A value to be used with the "FocalPlaneXResolution" tag.

static int

FOCAL_PLANE_RESOLUTION_UNIT_INCH

A value to be used with the "FocalPlaneXResolution" tag.

static int

FOCAL_PLANE_RESOLUTION_UNIT_NONE

A value to be used with the "FocalPlaneResolutionUnit" tag.

static int

GAIN_CONTROL_HIGH_GAIN_DOWN

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_HIGH_GAIN_UP

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_LOW_GAIN_DOWN

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_LOW_GAIN_UP

A value to be used with the "GainControl" tag.

static int

GAIN_CONTROL_NONE

A value to be used with the "GainControl" tag.

static int

LIGHT_SOURCE_CLOUDY_WEATHER

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D50

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D55

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D65

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_D75

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_DAYLIGHT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_FINE_WEATHER

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_FLASH

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_OTHER

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_SHADE

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_STANDARD_LIGHT_A

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_STANDARD_LIGHT_B

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_STANDARD_LIGHT_C

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_TUNGSTEN

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_UNKNOWN

A value to be used with the "LightSource" tag.

static int

LIGHT_SOURCE_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

static int

METERING_MODE_AVERAGE

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_CENTER_WEIGHTED_AVERAGE

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_MAX_RESERVED

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_MIN_RESERVED

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_MULTI_SPOT

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_OTHER

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_PARTIAL

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_PATTERN

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_SPOT

A value to be used with the "MeteringMode" tag.

static int

METERING_MODE_UNKNOWN

A value to be used with the "MeteringMode" tag.

static int

SATURATION_HIGH

A value to be used with the "Saturation" tag.

static int

SATURATION_LOW

A value to be used with the "Saturation" tag.

static int

SATURATION_NORMAL

A value to be used with the "Saturation" tag.

static int

SCENE_CAPTURE_TYPE_LANDSCAPE

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_CAPTURE_TYPE_NIGHT_SCENE

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_CAPTURE_TYPE_PORTRAIT

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_CAPTURE_TYPE_STANDARD

A value to be used with the "SceneCaptureType" tag.

static int

SCENE_TYPE_DSC

A value to be used with the "SceneType" tag.

static int

SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_NOT_DEFINED

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_TRILINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

static int

SHARPNESS_HARD

A value to be used with the "Sharpness" tag.

static int

SHARPNESS_NORMAL

A value to be used with the "Sharpness" tag.

static int

SHARPNESS_SOFT

A value to be used with the "Sharpness" tag.

static int

SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

A value to be used with the "SubjectDistanceRange" tag.

static int

SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

A value to be used with the "SubjectDistanceRange" tag.

static int

SUBJECT_DISTANCE_RANGE_MACRO

A value to be used with the "SubjectDistanceRange" tag.

static int

SUBJECT_DISTANCE_RANGE_UNKNOWN

A value to be used with the "SubjectDistanceRange" tag.

static int

TAG_APERTURE_VALUE

A tag indicating the lens aperture (type RATIONAL).

static int

TAG_BRIGHTNESS_VALUE

A tag indicating the value of brightness (type SRATIONAL).

static int

TAG_CFA_PATTERN

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

static int

TAG_COLOR_SPACE

A tag indicating the color space information (type SHORT).

static int

TAG_COMPONENTS_CONFIGURATION

A tag containing the components configuration information (type
UNDEFINED, count = 4).

static int

TAG_COMPRESSED_BITS_PER_PIXEL

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

static int

TAG_CONTRAST

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

static int

TAG_CUSTOM_RENDERED

A tag indicating the use of special processing on image data,
such as rendering geared to output.

static int

TAG_DATE_TIME_DIGITIZED

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

static int

TAG_DATE_TIME_ORIGINAL

A tag indicating the date and time when the original image was
generated (type ASCII).

static int

TAG_DEVICE_SETTING_DESCRIPTION

A tag indicating information on the picture-taking conditions
of a particular camera model.

static int

TAG_DIGITAL_ZOOM_RATIO

A tag indicating the digital zoom ratio when the image was shot.

static int

TAG_EXIF_VERSION

A tag containing the Exif version number (type UNDEFINED, count =
4).

static int

TAG_EXPOSURE_BIAS_VALUE

A tag indicating the exposure bias (type SRATIONAL).

static int

TAG_EXPOSURE_INDEX

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

static int

TAG_EXPOSURE_MODE

A tag indicating the exposure mode set when the image was shot.

static int

TAG_EXPOSURE_PROGRAM

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

static int

TAG_EXPOSURE_TIME

A tag indicating the exposure time, in seconds (type RATIONAL).

static int

TAG_F_NUMBER

A tag indicating the F number (type RATIONAL).

static int

TAG_FILE_SOURCE

A tag indicating the image source (type UNDEFINED).

static int

TAG_FLASH

A tag indicating the flash firing status and flash return
status (type SHORT).

static int

TAG_FLASH_ENERGY

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

static int

TAG_FLASHPIX_VERSION

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

static int

TAG_FOCAL_LENGTH

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

static int

TAG_FOCAL_LENGTH_IN_35MM_FILM

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

static int

TAG_FOCAL_PLANE_RESOLUTION_UNIT

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

static int

TAG_FOCAL_PLANE_X_RESOLUTION

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

static int

TAG_FOCAL_PLANE_Y_RESOLUTION

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

static int

TAG_GAIN_CONTROL

A tag indicating the degree of overall image gain adjustment.

static int

TAG_GPS_INFO_IFD_POINTER

A tag pointing to a GPS info IFD (type LONG).

static int

TAG_IMAGE_UNIQUE_ID

A tag indicating an identifier assigned uniquely to each image.

static int

TAG_INTEROPERABILITY_IFD_POINTER

A tag pointing to an interoperability IFD (type LONG).

static int

TAG_ISO_SPEED_RATINGS

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

static int

TAG_LIGHT_SOURCE

A tag indicatingthe kind of light source (type SHORT).

static int

TAG_MAKER_NOTE

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

static int

TAG_MARKER_NOTE

A tag indicating a manufacturer-defined marker note (type UNDEFINED).

static int

TAG_MAX_APERTURE_VALUE

A tag indicating the smallest F number of the lens (type
RATIONAL).

static int

TAG_METERING_MODE

A tag indicating the metering mode (type SHORT).

static int

TAG_OECF

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED).

static int

TAG_PIXEL_X_DIMENSION

A tag indicating the pixel X dimension (type SHORT or LONG).

static int

TAG_PIXEL_Y_DIMENSION

A tag indicating the pixel Y dimension (type SHORT or LONG).

static int

TAG_RELATED_SOUND_FILE

A tag indicating the name of a related sound file (type ASCII).

static int

TAG_SATURATION

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

static int

TAG_SCENE_CAPTURE_TYPE

A tag indicating the type of scene that was shot.

static int

TAG_SCENE_TYPE

A tag indicating the type of scene (type UNDEFINED).

static int

TAG_SENSING_METHOD

A tag indicating the sensor type on the camera or input device
(type SHORT).

static int

TAG_SHARPNESS

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

static int

TAG_SHUTTER_SPEED_VALUE

A tag indicating the shutter speed (type SRATIONAL).

static int

TAG_SPATIAL_FREQUENCY_RESPONSE

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

static int

TAG_SPECTRAL_SENSITIVITY

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII).

static int

TAG_SUB_SEC_TIME

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

static int

TAG_SUB_SEC_TIME_DIGITIZED

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

static int

TAG_SUB_SEC_TIME_ORIGINAL

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

static int

TAG_SUBJECT_AREA

A tag indicating the location and area of the main subject in
the overall scene.

static int

TAG_SUBJECT_DISTANCE

A tag indicating the distance to the subject, in meters (type
RATIONAL).

static int

TAG_SUBJECT_DISTANCE_RANGE

A tag indicating the distance to the subject.

static int

TAG_SUBJECT_LOCATION

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

static int

TAG_USER_COMMENT

A tag indicating a user comment (type UNDEFINED).

static int

TAG_WHITE_BALANCE

A tag indicating the white balance mode set when the image was shot.

static int

WHITE_BALANCE_AUTO

A value to be used with the "WhiteBalance" tag.

static int

WHITE_BALANCE_MANUAL

A value to be used with the "WhiteBalance" tag.

---

#### Field Summary

A value to be used with the "ColorSpace" tag.

A value to be used with the "ComponentsConfiguration" tag.

A value to be used with the "Contrast" tag.

A value to be used with the "CustomRendered" tag.

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1.

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2.

A value to be used with the "ExposureMode" tag.

A value to be used with the "ExposureProgram" tag.

A value to be used with the "FileSource" tag.

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

A mask to be used with the "Flash" tag, indicating that the
flash fired.

A mask to be used with the "Flash" tag, indicating no flash function
present.

A mask to be used with the "Flash" tag, indicating auto mode.

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

A value to be used with the "FocalPlaneXResolution" tag.

A value to be used with the "FocalPlaneResolutionUnit" tag.

A value to be used with the "GainControl" tag.

A value to be used with the "LightSource" tag.

A value to be used with the "MeteringMode" tag.

A value to be used with the "Saturation" tag.

A value to be used with the "SceneCaptureType" tag.

A value to be used with the "SceneType" tag.

A value to be used with the "SensingMethod" tag.

A value to be used with the "Sharpness" tag.

A value to be used with the "SubjectDistanceRange" tag.

A tag indicating the lens aperture (type RATIONAL).

A tag indicating the value of brightness (type SRATIONAL).

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

A tag indicating the color space information (type SHORT).

A tag containing the components configuration information (type
UNDEFINED, count = 4).

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

A tag indicating the use of special processing on image data,
such as rendering geared to output.

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

A tag indicating the date and time when the original image was
generated (type ASCII).

A tag indicating information on the picture-taking conditions
of a particular camera model.

A tag indicating the digital zoom ratio when the image was shot.

A tag containing the Exif version number (type UNDEFINED, count =
4).

A tag indicating the exposure bias (type SRATIONAL).

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

A tag indicating the exposure mode set when the image was shot.

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

A tag indicating the exposure time, in seconds (type RATIONAL).

A tag indicating the F number (type RATIONAL).

A tag indicating the image source (type UNDEFINED).

A tag indicating the flash firing status and flash return
status (type SHORT).

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

A tag indicating the degree of overall image gain adjustment.

A tag pointing to a GPS info IFD (type LONG).

A tag indicating an identifier assigned uniquely to each image.

A tag pointing to an interoperability IFD (type LONG).

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

A tag indicatingthe kind of light source (type SHORT).

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

A tag indicating a manufacturer-defined marker note (type UNDEFINED).

A tag indicating the smallest F number of the lens (type
RATIONAL).

A tag indicating the metering mode (type SHORT).

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED).

A tag indicating the pixel X dimension (type SHORT or LONG).

A tag indicating the pixel Y dimension (type SHORT or LONG).

A tag indicating the name of a related sound file (type ASCII).

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

A tag indicating the type of scene that was shot.

A tag indicating the type of scene (type UNDEFINED).

A tag indicating the sensor type on the camera or input device
(type SHORT).

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

A tag indicating the shutter speed (type SRATIONAL).

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII).

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

A tag indicating the location and area of the main subject in
the overall scene.

A tag indicating the distance to the subject, in meters (type
RATIONAL).

A tag indicating the distance to the subject.

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

A tag indicating a user comment (type UNDEFINED).

A tag indicating the white balance mode set when the image was shot.

A value to be used with the "WhiteBalance" tag.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ExifTIFFTagSet

getInstance

()

Returns a shared instance of an

ExifTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

Returns a shared instance of an

ExifTIFFTagSet

.

Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

---

#### Methods declared in class javax.imageio.plugins.tiff. TIFFTagSet

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

============ FIELD DETAIL ===========

- Field Detail

- TAG_GPS_INFO_IFD_POINTER

```java
public static final int TAG_GPS_INFO_IFD_POINTER
```

A tag pointing to a GPS info IFD (type LONG). This tag has
been superseded by

ExifParentTIFFTagSet.TAG_GPS_INFO_IFD_POINTER

.

**See Also:** Constant Field Values

- TAG_INTEROPERABILITY_IFD_POINTER

```java
public static final int TAG_INTEROPERABILITY_IFD_POINTER
```

A tag pointing to an interoperability IFD (type LONG).

**See Also:** Constant Field Values

- TAG_EXIF_VERSION

```java
public static final int TAG_EXIF_VERSION
```

A tag containing the Exif version number (type UNDEFINED, count =
4). Conformance to the Exif 2.1 standard is indicated using
the ASCII value "0210" (with no terminating NUL).

**See Also:** EXIF_VERSION_2_1

,

EXIF_VERSION_2_2

,

Constant Field Values

- EXIF_VERSION_2_1

```java
public static final
String
EXIF_VERSION_2_1
```

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1. The value equals the US-ASCII encoding of the byte array

{'0', '2', '1', '0'}

.

**See Also:** TAG_EXIF_VERSION

,

Constant Field Values

- EXIF_VERSION_2_2

```java
public static final
String
EXIF_VERSION_2_2
```

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2. The value equals the US-ASCII encoding of the byte array

{'0', '2', '2', '0'}

.

**See Also:** TAG_EXIF_VERSION

,

Constant Field Values

- TAG_FLASHPIX_VERSION

```java
public static final int TAG_FLASHPIX_VERSION
```

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

**See Also:** Constant Field Values

- TAG_COLOR_SPACE

```java
public static final int TAG_COLOR_SPACE
```

A tag indicating the color space information (type SHORT). The
legal values are given by the

COLOR_SPACE_*

constants.

**See Also:** COLOR_SPACE_SRGB

,

COLOR_SPACE_UNCALIBRATED

,

Constant Field Values

- COLOR_SPACE_SRGB

```java
public static final int COLOR_SPACE_SRGB
```

A value to be used with the "ColorSpace" tag.

**See Also:** TAG_COLOR_SPACE

,

Constant Field Values

- COLOR_SPACE_UNCALIBRATED

```java
public static final int COLOR_SPACE_UNCALIBRATED
```

A value to be used with the "ColorSpace" tag.

**See Also:** TAG_COLOR_SPACE

,

Constant Field Values

- TAG_COMPONENTS_CONFIGURATION

```java
public static final int TAG_COMPONENTS_CONFIGURATION
```

A tag containing the components configuration information (type
UNDEFINED, count = 4).

**See Also:** COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

,

COMPONENTS_CONFIGURATION_Y

,

COMPONENTS_CONFIGURATION_CB

,

COMPONENTS_CONFIGURATION_CR

,

COMPONENTS_CONFIGURATION_R

,

COMPONENTS_CONFIGURATION_G

,

COMPONENTS_CONFIGURATION_B

,

Constant Field Values

- COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

```java
public static final int COMPONENTS_CONFIGURATION_DOES_NOT_EXIST
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_Y

```java
public static final int COMPONENTS_CONFIGURATION_Y
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_CB

```java
public static final int COMPONENTS_CONFIGURATION_CB
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_CR

```java
public static final int COMPONENTS_CONFIGURATION_CR
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_R

```java
public static final int COMPONENTS_CONFIGURATION_R
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_G

```java
public static final int COMPONENTS_CONFIGURATION_G
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_B

```java
public static final int COMPONENTS_CONFIGURATION_B
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- TAG_COMPRESSED_BITS_PER_PIXEL

```java
public static final int TAG_COMPRESSED_BITS_PER_PIXEL
```

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

**See Also:** Constant Field Values

- TAG_PIXEL_X_DIMENSION

```java
public static final int TAG_PIXEL_X_DIMENSION
```

A tag indicating the pixel X dimension (type SHORT or LONG).
This value records the valid width of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:** Constant Field Values

- TAG_PIXEL_Y_DIMENSION

```java
public static final int TAG_PIXEL_Y_DIMENSION
```

A tag indicating the pixel Y dimension (type SHORT or LONG).
This value records the valid height of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:** Constant Field Values

- TAG_MAKER_NOTE

```java
public static final int TAG_MAKER_NOTE
```

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

**See Also:** Constant Field Values

- TAG_MARKER_NOTE

```java
public static final int TAG_MARKER_NOTE
```

A tag indicating a manufacturer-defined marker note (type UNDEFINED).
This tag has been superseded by

TAG_MAKER_NOTE

.

**See Also:** Constant Field Values

- TAG_USER_COMMENT

```java
public static final int TAG_USER_COMMENT
```

A tag indicating a user comment (type UNDEFINED). The first 8
bytes are used to specify the character encoding.

**See Also:** Constant Field Values

- TAG_RELATED_SOUND_FILE

```java
public static final int TAG_RELATED_SOUND_FILE
```

A tag indicating the name of a related sound file (type ASCII).

**See Also:** Constant Field Values

- TAG_DATE_TIME_ORIGINAL

```java
public static final int TAG_DATE_TIME_ORIGINAL
```

A tag indicating the date and time when the original image was
generated (type ASCII).

**See Also:** Constant Field Values

- TAG_DATE_TIME_DIGITIZED

```java
public static final int TAG_DATE_TIME_DIGITIZED
```

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

**See Also:** Constant Field Values

- TAG_SUB_SEC_TIME

```java
public static final int TAG_SUB_SEC_TIME
```

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

**See Also:** Constant Field Values

- TAG_SUB_SEC_TIME_ORIGINAL

```java
public static final int TAG_SUB_SEC_TIME_ORIGINAL
```

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

**See Also:** Constant Field Values

- TAG_SUB_SEC_TIME_DIGITIZED

```java
public static final int TAG_SUB_SEC_TIME_DIGITIZED
```

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

**See Also:** Constant Field Values

- TAG_EXPOSURE_TIME

```java
public static final int TAG_EXPOSURE_TIME
```

A tag indicating the exposure time, in seconds (type RATIONAL).

**See Also:** Constant Field Values

- TAG_F_NUMBER

```java
public static final int TAG_F_NUMBER
```

A tag indicating the F number (type RATIONAL).

**See Also:** Constant Field Values

- TAG_EXPOSURE_PROGRAM

```java
public static final int TAG_EXPOSURE_PROGRAM
```

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

**See Also:** EXPOSURE_PROGRAM_NOT_DEFINED

,

EXPOSURE_PROGRAM_MANUAL

,

EXPOSURE_PROGRAM_NORMAL_PROGRAM

,

EXPOSURE_PROGRAM_APERTURE_PRIORITY

,

EXPOSURE_PROGRAM_SHUTTER_PRIORITY

,

EXPOSURE_PROGRAM_CREATIVE_PROGRAM

,

EXPOSURE_PROGRAM_ACTION_PROGRAM

,

EXPOSURE_PROGRAM_PORTRAIT_MODE

,

EXPOSURE_PROGRAM_LANDSCAPE_MODE

,

EXPOSURE_PROGRAM_MAX_RESERVED

,

Constant Field Values

- EXPOSURE_PROGRAM_NOT_DEFINED

```java
public static final int EXPOSURE_PROGRAM_NOT_DEFINED
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_MANUAL

```java
public static final int EXPOSURE_PROGRAM_MANUAL
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_NORMAL_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_NORMAL_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_APERTURE_PRIORITY

```java
public static final int EXPOSURE_PROGRAM_APERTURE_PRIORITY
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_SHUTTER_PRIORITY

```java
public static final int EXPOSURE_PROGRAM_SHUTTER_PRIORITY
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_CREATIVE_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_CREATIVE_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_ACTION_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_ACTION_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_PORTRAIT_MODE

```java
public static final int EXPOSURE_PROGRAM_PORTRAIT_MODE
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_LANDSCAPE_MODE

```java
public static final int EXPOSURE_PROGRAM_LANDSCAPE_MODE
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_MAX_RESERVED

```java
public static final int EXPOSURE_PROGRAM_MAX_RESERVED
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- TAG_SPECTRAL_SENSITIVITY

```java
public static final int TAG_SPECTRAL_SENSITIVITY
```

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII). The tag value is an ASCII string
compatible with the ASTM standard.

**See Also:** Constant Field Values

- TAG_ISO_SPEED_RATINGS

```java
public static final int TAG_ISO_SPEED_RATINGS
```

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

**See Also:** Constant Field Values

- TAG_OECF

```java
public static final int TAG_OECF
```

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED). OECF is
the relationship between the camera optical input and the image
values.

**See Also:** Constant Field Values

- TAG_SHUTTER_SPEED_VALUE

```java
public static final int TAG_SHUTTER_SPEED_VALUE
```

A tag indicating the shutter speed (type SRATIONAL).

**See Also:** Constant Field Values

- TAG_APERTURE_VALUE

```java
public static final int TAG_APERTURE_VALUE
```

A tag indicating the lens aperture (type RATIONAL).

**See Also:** Constant Field Values

- TAG_BRIGHTNESS_VALUE

```java
public static final int TAG_BRIGHTNESS_VALUE
```

A tag indicating the value of brightness (type SRATIONAL).

**See Also:** Constant Field Values

- TAG_EXPOSURE_BIAS_VALUE

```java
public static final int TAG_EXPOSURE_BIAS_VALUE
```

A tag indicating the exposure bias (type SRATIONAL).

**See Also:** Constant Field Values

- TAG_MAX_APERTURE_VALUE

```java
public static final int TAG_MAX_APERTURE_VALUE
```

A tag indicating the smallest F number of the lens (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_SUBJECT_DISTANCE

```java
public static final int TAG_SUBJECT_DISTANCE
```

A tag indicating the distance to the subject, in meters (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_METERING_MODE

```java
public static final int TAG_METERING_MODE
```

A tag indicating the metering mode (type SHORT).

**See Also:** METERING_MODE_UNKNOWN

,

METERING_MODE_AVERAGE

,

METERING_MODE_CENTER_WEIGHTED_AVERAGE

,

METERING_MODE_SPOT

,

METERING_MODE_MULTI_SPOT

,

METERING_MODE_PATTERN

,

METERING_MODE_PARTIAL

,

METERING_MODE_MIN_RESERVED

,

METERING_MODE_MAX_RESERVED

,

METERING_MODE_OTHER

,

Constant Field Values

- METERING_MODE_UNKNOWN

```java
public static final int METERING_MODE_UNKNOWN
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_AVERAGE

```java
public static final int METERING_MODE_AVERAGE
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_CENTER_WEIGHTED_AVERAGE

```java
public static final int METERING_MODE_CENTER_WEIGHTED_AVERAGE
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_SPOT

```java
public static final int METERING_MODE_SPOT
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_MULTI_SPOT

```java
public static final int METERING_MODE_MULTI_SPOT
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_PATTERN

```java
public static final int METERING_MODE_PATTERN
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_PARTIAL

```java
public static final int METERING_MODE_PARTIAL
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_MIN_RESERVED

```java
public static final int METERING_MODE_MIN_RESERVED
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_MAX_RESERVED

```java
public static final int METERING_MODE_MAX_RESERVED
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_OTHER

```java
public static final int METERING_MODE_OTHER
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- TAG_LIGHT_SOURCE

```java
public static final int TAG_LIGHT_SOURCE
```

A tag indicatingthe kind of light source (type SHORT).

**See Also:** LIGHT_SOURCE_UNKNOWN

,

LIGHT_SOURCE_DAYLIGHT

,

LIGHT_SOURCE_FLUORESCENT

,

LIGHT_SOURCE_TUNGSTEN

,

LIGHT_SOURCE_STANDARD_LIGHT_A

,

LIGHT_SOURCE_STANDARD_LIGHT_B

,

LIGHT_SOURCE_STANDARD_LIGHT_C

,

LIGHT_SOURCE_D55

,

LIGHT_SOURCE_D65

,

LIGHT_SOURCE_D75

,

LIGHT_SOURCE_OTHER

,

Constant Field Values

- LIGHT_SOURCE_UNKNOWN

```java
public static final int LIGHT_SOURCE_UNKNOWN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_DAYLIGHT

```java
public static final int LIGHT_SOURCE_DAYLIGHT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_TUNGSTEN

```java
public static final int LIGHT_SOURCE_TUNGSTEN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_FLASH

```java
public static final int LIGHT_SOURCE_FLASH
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_FINE_WEATHER

```java
public static final int LIGHT_SOURCE_FINE_WEATHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_CLOUDY_WEATHER

```java
public static final int LIGHT_SOURCE_CLOUDY_WEATHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_SHADE

```java
public static final int LIGHT_SOURCE_SHADE
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

```java
public static final int LIGHT_SOURCE_DAYLIGHT_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_DAY_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_COOL_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_STANDARD_LIGHT_A

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_A
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_STANDARD_LIGHT_B

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_B
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_STANDARD_LIGHT_C

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_C
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D55

```java
public static final int LIGHT_SOURCE_D55
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D65

```java
public static final int LIGHT_SOURCE_D65
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D75

```java
public static final int LIGHT_SOURCE_D75
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D50

```java
public static final int LIGHT_SOURCE_D50
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

```java
public static final int LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_OTHER

```java
public static final int LIGHT_SOURCE_OTHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- TAG_FLASH

```java
public static final int TAG_FLASH
```

A tag indicating the flash firing status and flash return
status (type SHORT).

**See Also:** FLASH_DID_NOT_FIRE

,

FLASH_FIRED

,

FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

,

FLASH_STROBE_RETURN_LIGHT_DETECTED

,

Constant Field Values

- FLASH_DID_NOT_FIRE

```java
public static final int FLASH_DID_NOT_FIRE
```

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_FIRED

```java
public static final int FLASH_FIRED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

```java
public static final int FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_STROBE_RETURN_LIGHT_DETECTED

```java
public static final int FLASH_STROBE_RETURN_LIGHT_DETECTED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_FIRED

```java
public static final int FLASH_MASK_FIRED
```

A mask to be used with the "Flash" tag, indicating that the
flash fired.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_RETURN_NOT_DETECTED

```java
public static final int FLASH_MASK_RETURN_NOT_DETECTED
```

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_RETURN_DETECTED

```java
public static final int FLASH_MASK_RETURN_DETECTED
```

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_MODE_FLASH_FIRING

```java
public static final int FLASH_MASK_MODE_FLASH_FIRING
```

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_MODE_FLASH_SUPPRESSION

```java
public static final int FLASH_MASK_MODE_FLASH_SUPPRESSION
```

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_MODE_AUTO

```java
public static final int FLASH_MASK_MODE_AUTO
```

A mask to be used with the "Flash" tag, indicating auto mode.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_FUNCTION_NOT_PRESENT

```java
public static final int FLASH_MASK_FUNCTION_NOT_PRESENT
```

A mask to be used with the "Flash" tag, indicating no flash function
present.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_RED_EYE_REDUCTION

```java
public static final int FLASH_MASK_RED_EYE_REDUCTION
```

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

**See Also:** TAG_FLASH

,

Constant Field Values

- TAG_FOCAL_LENGTH

```java
public static final int TAG_FOCAL_LENGTH
```

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

**See Also:** Constant Field Values

- TAG_SUBJECT_AREA

```java
public static final int TAG_SUBJECT_AREA
```

A tag indicating the location and area of the main subject in
the overall scene.

**See Also:** Constant Field Values

- TAG_FLASH_ENERGY

```java
public static final int TAG_FLASH_ENERGY
```

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_SPATIAL_FREQUENCY_RESPONSE

```java
public static final int TAG_SPATIAL_FREQUENCY_RESPONSE
```

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

**See Also:** Constant Field Values

- TAG_FOCAL_PLANE_X_RESOLUTION

```java
public static final int TAG_FOCAL_PLANE_X_RESOLUTION
```

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_FOCAL_PLANE_Y_RESOLUTION

```java
public static final int TAG_FOCAL_PLANE_Y_RESOLUTION
```

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_FOCAL_PLANE_RESOLUTION_UNIT

```java
public static final int TAG_FOCAL_PLANE_RESOLUTION_UNIT
```

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

**See Also:** FOCAL_PLANE_RESOLUTION_UNIT_NONE

,

FOCAL_PLANE_RESOLUTION_UNIT_INCH

,

FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

- FOCAL_PLANE_RESOLUTION_UNIT_NONE

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_NONE
```

A value to be used with the "FocalPlaneResolutionUnit" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

- FOCAL_PLANE_RESOLUTION_UNIT_INCH

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_INCH
```

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

- FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER
```

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

- TAG_SUBJECT_LOCATION

```java
public static final int TAG_SUBJECT_LOCATION
```

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

**See Also:** Constant Field Values

- TAG_EXPOSURE_INDEX

```java
public static final int TAG_EXPOSURE_INDEX
```

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_SENSING_METHOD

```java
public static final int TAG_SENSING_METHOD
```

A tag indicating the sensor type on the camera or input device
(type SHORT).

**See Also:** SENSING_METHOD_NOT_DEFINED

,

SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

,

SENSING_METHOD_TRILINEAR_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

,

Constant Field Values

- SENSING_METHOD_NOT_DEFINED

```java
public static final int SENSING_METHOD_NOT_DEFINED
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

```java
public static final int SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_TRILINEAR_SENSOR

```java
public static final int SENSING_METHOD_TRILINEAR_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

```java
public static final int SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- TAG_FILE_SOURCE

```java
public static final int TAG_FILE_SOURCE
```

A tag indicating the image source (type UNDEFINED).

**See Also:** FILE_SOURCE_DSC

,

Constant Field Values

- FILE_SOURCE_DSC

```java
public static final int FILE_SOURCE_DSC
```

A value to be used with the "FileSource" tag.

**See Also:** TAG_FILE_SOURCE

,

Constant Field Values

- TAG_SCENE_TYPE

```java
public static final int TAG_SCENE_TYPE
```

A tag indicating the type of scene (type UNDEFINED).

**See Also:** SCENE_TYPE_DSC

,

Constant Field Values

- SCENE_TYPE_DSC

```java
public static final int SCENE_TYPE_DSC
```

A value to be used with the "SceneType" tag.

**See Also:** TAG_SCENE_TYPE

,

Constant Field Values

- TAG_CFA_PATTERN

```java
public static final int TAG_CFA_PATTERN
```

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

**See Also:** Constant Field Values

- TAG_CUSTOM_RENDERED

```java
public static final int TAG_CUSTOM_RENDERED
```

A tag indicating the use of special processing on image data,
such as rendering geared to output.

**See Also:** Constant Field Values

- CUSTOM_RENDERED_NORMAL

```java
public static final int CUSTOM_RENDERED_NORMAL
```

A value to be used with the "CustomRendered" tag.

**See Also:** TAG_CUSTOM_RENDERED

,

Constant Field Values

- CUSTOM_RENDERED_CUSTOM

```java
public static final int CUSTOM_RENDERED_CUSTOM
```

A value to be used with the "CustomRendered" tag.

**See Also:** TAG_CUSTOM_RENDERED

,

Constant Field Values

- TAG_EXPOSURE_MODE

```java
public static final int TAG_EXPOSURE_MODE
```

A tag indicating the exposure mode set when the image was shot.

**See Also:** Constant Field Values

- EXPOSURE_MODE_AUTO_EXPOSURE

```java
public static final int EXPOSURE_MODE_AUTO_EXPOSURE
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

- EXPOSURE_MODE_MANUAL_EXPOSURE

```java
public static final int EXPOSURE_MODE_MANUAL_EXPOSURE
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

- EXPOSURE_MODE_AUTO_BRACKET

```java
public static final int EXPOSURE_MODE_AUTO_BRACKET
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

- TAG_WHITE_BALANCE

```java
public static final int TAG_WHITE_BALANCE
```

A tag indicating the white balance mode set when the image was shot.

**See Also:** Constant Field Values

- WHITE_BALANCE_AUTO

```java
public static final int WHITE_BALANCE_AUTO
```

A value to be used with the "WhiteBalance" tag.

**See Also:** TAG_WHITE_BALANCE

,

Constant Field Values

- WHITE_BALANCE_MANUAL

```java
public static final int WHITE_BALANCE_MANUAL
```

A value to be used with the "WhiteBalance" tag.

**See Also:** TAG_WHITE_BALANCE

,

Constant Field Values

- TAG_DIGITAL_ZOOM_RATIO

```java
public static final int TAG_DIGITAL_ZOOM_RATIO
```

A tag indicating the digital zoom ratio when the image was shot.

**See Also:** Constant Field Values

- TAG_FOCAL_LENGTH_IN_35MM_FILM

```java
public static final int TAG_FOCAL_LENGTH_IN_35MM_FILM
```

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

**See Also:** Constant Field Values

- TAG_SCENE_CAPTURE_TYPE

```java
public static final int TAG_SCENE_CAPTURE_TYPE
```

A tag indicating the type of scene that was shot.

**See Also:** Constant Field Values

- SCENE_CAPTURE_TYPE_STANDARD

```java
public static final int SCENE_CAPTURE_TYPE_STANDARD
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- SCENE_CAPTURE_TYPE_LANDSCAPE

```java
public static final int SCENE_CAPTURE_TYPE_LANDSCAPE
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- SCENE_CAPTURE_TYPE_PORTRAIT

```java
public static final int SCENE_CAPTURE_TYPE_PORTRAIT
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- SCENE_CAPTURE_TYPE_NIGHT_SCENE

```java
public static final int SCENE_CAPTURE_TYPE_NIGHT_SCENE
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- TAG_GAIN_CONTROL

```java
public static final int TAG_GAIN_CONTROL
```

A tag indicating the degree of overall image gain adjustment.

**See Also:** Constant Field Values

- GAIN_CONTROL_NONE

```java
public static final int GAIN_CONTROL_NONE
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_LOW_GAIN_UP

```java
public static final int GAIN_CONTROL_LOW_GAIN_UP
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_HIGH_GAIN_UP

```java
public static final int GAIN_CONTROL_HIGH_GAIN_UP
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_LOW_GAIN_DOWN

```java
public static final int GAIN_CONTROL_LOW_GAIN_DOWN
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_HIGH_GAIN_DOWN

```java
public static final int GAIN_CONTROL_HIGH_GAIN_DOWN
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- TAG_CONTRAST

```java
public static final int TAG_CONTRAST
```

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

**See Also:** Constant Field Values

- CONTRAST_NORMAL

```java
public static final int CONTRAST_NORMAL
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

- CONTRAST_SOFT

```java
public static final int CONTRAST_SOFT
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

- CONTRAST_HARD

```java
public static final int CONTRAST_HARD
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

- TAG_SATURATION

```java
public static final int TAG_SATURATION
```

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

**See Also:** Constant Field Values

- SATURATION_NORMAL

```java
public static final int SATURATION_NORMAL
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

- SATURATION_LOW

```java
public static final int SATURATION_LOW
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

- SATURATION_HIGH

```java
public static final int SATURATION_HIGH
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

- TAG_SHARPNESS

```java
public static final int TAG_SHARPNESS
```

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

**See Also:** Constant Field Values

- SHARPNESS_NORMAL

```java
public static final int SHARPNESS_NORMAL
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

- SHARPNESS_SOFT

```java
public static final int SHARPNESS_SOFT
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

- SHARPNESS_HARD

```java
public static final int SHARPNESS_HARD
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

- TAG_DEVICE_SETTING_DESCRIPTION

```java
public static final int TAG_DEVICE_SETTING_DESCRIPTION
```

A tag indicating information on the picture-taking conditions
of a particular camera model.

**See Also:** Constant Field Values

- TAG_SUBJECT_DISTANCE_RANGE

```java
public static final int TAG_SUBJECT_DISTANCE_RANGE
```

A tag indicating the distance to the subject.

**See Also:** Constant Field Values

- SUBJECT_DISTANCE_RANGE_UNKNOWN

```java
public static final int SUBJECT_DISTANCE_RANGE_UNKNOWN
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- SUBJECT_DISTANCE_RANGE_MACRO

```java
public static final int SUBJECT_DISTANCE_RANGE_MACRO
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

```java
public static final int SUBJECT_DISTANCE_RANGE_CLOSE_VIEW
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

```java
public static final int SUBJECT_DISTANCE_RANGE_DISTANT_VIEW
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- TAG_IMAGE_UNIQUE_ID

```java
public static final int TAG_IMAGE_UNIQUE_ID
```

A tag indicating an identifier assigned uniquely to each image.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
ExifTIFFTagSet
getInstance()
```

Returns a shared instance of an

ExifTIFFTagSet

.

**Returns:** an

ExifTIFFTagSet

instance.

Field Detail

- TAG_GPS_INFO_IFD_POINTER

```java
public static final int TAG_GPS_INFO_IFD_POINTER
```

A tag pointing to a GPS info IFD (type LONG). This tag has
been superseded by

ExifParentTIFFTagSet.TAG_GPS_INFO_IFD_POINTER

.

**See Also:** Constant Field Values

- TAG_INTEROPERABILITY_IFD_POINTER

```java
public static final int TAG_INTEROPERABILITY_IFD_POINTER
```

A tag pointing to an interoperability IFD (type LONG).

**See Also:** Constant Field Values

- TAG_EXIF_VERSION

```java
public static final int TAG_EXIF_VERSION
```

A tag containing the Exif version number (type UNDEFINED, count =
4). Conformance to the Exif 2.1 standard is indicated using
the ASCII value "0210" (with no terminating NUL).

**See Also:** EXIF_VERSION_2_1

,

EXIF_VERSION_2_2

,

Constant Field Values

- EXIF_VERSION_2_1

```java
public static final
String
EXIF_VERSION_2_1
```

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1. The value equals the US-ASCII encoding of the byte array

{'0', '2', '1', '0'}

.

**See Also:** TAG_EXIF_VERSION

,

Constant Field Values

- EXIF_VERSION_2_2

```java
public static final
String
EXIF_VERSION_2_2
```

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2. The value equals the US-ASCII encoding of the byte array

{'0', '2', '2', '0'}

.

**See Also:** TAG_EXIF_VERSION

,

Constant Field Values

- TAG_FLASHPIX_VERSION

```java
public static final int TAG_FLASHPIX_VERSION
```

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

**See Also:** Constant Field Values

- TAG_COLOR_SPACE

```java
public static final int TAG_COLOR_SPACE
```

A tag indicating the color space information (type SHORT). The
legal values are given by the

COLOR_SPACE_*

constants.

**See Also:** COLOR_SPACE_SRGB

,

COLOR_SPACE_UNCALIBRATED

,

Constant Field Values

- COLOR_SPACE_SRGB

```java
public static final int COLOR_SPACE_SRGB
```

A value to be used with the "ColorSpace" tag.

**See Also:** TAG_COLOR_SPACE

,

Constant Field Values

- COLOR_SPACE_UNCALIBRATED

```java
public static final int COLOR_SPACE_UNCALIBRATED
```

A value to be used with the "ColorSpace" tag.

**See Also:** TAG_COLOR_SPACE

,

Constant Field Values

- TAG_COMPONENTS_CONFIGURATION

```java
public static final int TAG_COMPONENTS_CONFIGURATION
```

A tag containing the components configuration information (type
UNDEFINED, count = 4).

**See Also:** COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

,

COMPONENTS_CONFIGURATION_Y

,

COMPONENTS_CONFIGURATION_CB

,

COMPONENTS_CONFIGURATION_CR

,

COMPONENTS_CONFIGURATION_R

,

COMPONENTS_CONFIGURATION_G

,

COMPONENTS_CONFIGURATION_B

,

Constant Field Values

- COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

```java
public static final int COMPONENTS_CONFIGURATION_DOES_NOT_EXIST
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_Y

```java
public static final int COMPONENTS_CONFIGURATION_Y
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_CB

```java
public static final int COMPONENTS_CONFIGURATION_CB
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_CR

```java
public static final int COMPONENTS_CONFIGURATION_CR
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_R

```java
public static final int COMPONENTS_CONFIGURATION_R
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_G

```java
public static final int COMPONENTS_CONFIGURATION_G
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- COMPONENTS_CONFIGURATION_B

```java
public static final int COMPONENTS_CONFIGURATION_B
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

- TAG_COMPRESSED_BITS_PER_PIXEL

```java
public static final int TAG_COMPRESSED_BITS_PER_PIXEL
```

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

**See Also:** Constant Field Values

- TAG_PIXEL_X_DIMENSION

```java
public static final int TAG_PIXEL_X_DIMENSION
```

A tag indicating the pixel X dimension (type SHORT or LONG).
This value records the valid width of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:** Constant Field Values

- TAG_PIXEL_Y_DIMENSION

```java
public static final int TAG_PIXEL_Y_DIMENSION
```

A tag indicating the pixel Y dimension (type SHORT or LONG).
This value records the valid height of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:** Constant Field Values

- TAG_MAKER_NOTE

```java
public static final int TAG_MAKER_NOTE
```

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

**See Also:** Constant Field Values

- TAG_MARKER_NOTE

```java
public static final int TAG_MARKER_NOTE
```

A tag indicating a manufacturer-defined marker note (type UNDEFINED).
This tag has been superseded by

TAG_MAKER_NOTE

.

**See Also:** Constant Field Values

- TAG_USER_COMMENT

```java
public static final int TAG_USER_COMMENT
```

A tag indicating a user comment (type UNDEFINED). The first 8
bytes are used to specify the character encoding.

**See Also:** Constant Field Values

- TAG_RELATED_SOUND_FILE

```java
public static final int TAG_RELATED_SOUND_FILE
```

A tag indicating the name of a related sound file (type ASCII).

**See Also:** Constant Field Values

- TAG_DATE_TIME_ORIGINAL

```java
public static final int TAG_DATE_TIME_ORIGINAL
```

A tag indicating the date and time when the original image was
generated (type ASCII).

**See Also:** Constant Field Values

- TAG_DATE_TIME_DIGITIZED

```java
public static final int TAG_DATE_TIME_DIGITIZED
```

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

**See Also:** Constant Field Values

- TAG_SUB_SEC_TIME

```java
public static final int TAG_SUB_SEC_TIME
```

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

**See Also:** Constant Field Values

- TAG_SUB_SEC_TIME_ORIGINAL

```java
public static final int TAG_SUB_SEC_TIME_ORIGINAL
```

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

**See Also:** Constant Field Values

- TAG_SUB_SEC_TIME_DIGITIZED

```java
public static final int TAG_SUB_SEC_TIME_DIGITIZED
```

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

**See Also:** Constant Field Values

- TAG_EXPOSURE_TIME

```java
public static final int TAG_EXPOSURE_TIME
```

A tag indicating the exposure time, in seconds (type RATIONAL).

**See Also:** Constant Field Values

- TAG_F_NUMBER

```java
public static final int TAG_F_NUMBER
```

A tag indicating the F number (type RATIONAL).

**See Also:** Constant Field Values

- TAG_EXPOSURE_PROGRAM

```java
public static final int TAG_EXPOSURE_PROGRAM
```

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

**See Also:** EXPOSURE_PROGRAM_NOT_DEFINED

,

EXPOSURE_PROGRAM_MANUAL

,

EXPOSURE_PROGRAM_NORMAL_PROGRAM

,

EXPOSURE_PROGRAM_APERTURE_PRIORITY

,

EXPOSURE_PROGRAM_SHUTTER_PRIORITY

,

EXPOSURE_PROGRAM_CREATIVE_PROGRAM

,

EXPOSURE_PROGRAM_ACTION_PROGRAM

,

EXPOSURE_PROGRAM_PORTRAIT_MODE

,

EXPOSURE_PROGRAM_LANDSCAPE_MODE

,

EXPOSURE_PROGRAM_MAX_RESERVED

,

Constant Field Values

- EXPOSURE_PROGRAM_NOT_DEFINED

```java
public static final int EXPOSURE_PROGRAM_NOT_DEFINED
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_MANUAL

```java
public static final int EXPOSURE_PROGRAM_MANUAL
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_NORMAL_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_NORMAL_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_APERTURE_PRIORITY

```java
public static final int EXPOSURE_PROGRAM_APERTURE_PRIORITY
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_SHUTTER_PRIORITY

```java
public static final int EXPOSURE_PROGRAM_SHUTTER_PRIORITY
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_CREATIVE_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_CREATIVE_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_ACTION_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_ACTION_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_PORTRAIT_MODE

```java
public static final int EXPOSURE_PROGRAM_PORTRAIT_MODE
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_LANDSCAPE_MODE

```java
public static final int EXPOSURE_PROGRAM_LANDSCAPE_MODE
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- EXPOSURE_PROGRAM_MAX_RESERVED

```java
public static final int EXPOSURE_PROGRAM_MAX_RESERVED
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

- TAG_SPECTRAL_SENSITIVITY

```java
public static final int TAG_SPECTRAL_SENSITIVITY
```

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII). The tag value is an ASCII string
compatible with the ASTM standard.

**See Also:** Constant Field Values

- TAG_ISO_SPEED_RATINGS

```java
public static final int TAG_ISO_SPEED_RATINGS
```

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

**See Also:** Constant Field Values

- TAG_OECF

```java
public static final int TAG_OECF
```

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED). OECF is
the relationship between the camera optical input and the image
values.

**See Also:** Constant Field Values

- TAG_SHUTTER_SPEED_VALUE

```java
public static final int TAG_SHUTTER_SPEED_VALUE
```

A tag indicating the shutter speed (type SRATIONAL).

**See Also:** Constant Field Values

- TAG_APERTURE_VALUE

```java
public static final int TAG_APERTURE_VALUE
```

A tag indicating the lens aperture (type RATIONAL).

**See Also:** Constant Field Values

- TAG_BRIGHTNESS_VALUE

```java
public static final int TAG_BRIGHTNESS_VALUE
```

A tag indicating the value of brightness (type SRATIONAL).

**See Also:** Constant Field Values

- TAG_EXPOSURE_BIAS_VALUE

```java
public static final int TAG_EXPOSURE_BIAS_VALUE
```

A tag indicating the exposure bias (type SRATIONAL).

**See Also:** Constant Field Values

- TAG_MAX_APERTURE_VALUE

```java
public static final int TAG_MAX_APERTURE_VALUE
```

A tag indicating the smallest F number of the lens (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_SUBJECT_DISTANCE

```java
public static final int TAG_SUBJECT_DISTANCE
```

A tag indicating the distance to the subject, in meters (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_METERING_MODE

```java
public static final int TAG_METERING_MODE
```

A tag indicating the metering mode (type SHORT).

**See Also:** METERING_MODE_UNKNOWN

,

METERING_MODE_AVERAGE

,

METERING_MODE_CENTER_WEIGHTED_AVERAGE

,

METERING_MODE_SPOT

,

METERING_MODE_MULTI_SPOT

,

METERING_MODE_PATTERN

,

METERING_MODE_PARTIAL

,

METERING_MODE_MIN_RESERVED

,

METERING_MODE_MAX_RESERVED

,

METERING_MODE_OTHER

,

Constant Field Values

- METERING_MODE_UNKNOWN

```java
public static final int METERING_MODE_UNKNOWN
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_AVERAGE

```java
public static final int METERING_MODE_AVERAGE
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_CENTER_WEIGHTED_AVERAGE

```java
public static final int METERING_MODE_CENTER_WEIGHTED_AVERAGE
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_SPOT

```java
public static final int METERING_MODE_SPOT
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_MULTI_SPOT

```java
public static final int METERING_MODE_MULTI_SPOT
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_PATTERN

```java
public static final int METERING_MODE_PATTERN
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_PARTIAL

```java
public static final int METERING_MODE_PARTIAL
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_MIN_RESERVED

```java
public static final int METERING_MODE_MIN_RESERVED
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_MAX_RESERVED

```java
public static final int METERING_MODE_MAX_RESERVED
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- METERING_MODE_OTHER

```java
public static final int METERING_MODE_OTHER
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

- TAG_LIGHT_SOURCE

```java
public static final int TAG_LIGHT_SOURCE
```

A tag indicatingthe kind of light source (type SHORT).

**See Also:** LIGHT_SOURCE_UNKNOWN

,

LIGHT_SOURCE_DAYLIGHT

,

LIGHT_SOURCE_FLUORESCENT

,

LIGHT_SOURCE_TUNGSTEN

,

LIGHT_SOURCE_STANDARD_LIGHT_A

,

LIGHT_SOURCE_STANDARD_LIGHT_B

,

LIGHT_SOURCE_STANDARD_LIGHT_C

,

LIGHT_SOURCE_D55

,

LIGHT_SOURCE_D65

,

LIGHT_SOURCE_D75

,

LIGHT_SOURCE_OTHER

,

Constant Field Values

- LIGHT_SOURCE_UNKNOWN

```java
public static final int LIGHT_SOURCE_UNKNOWN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_DAYLIGHT

```java
public static final int LIGHT_SOURCE_DAYLIGHT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_TUNGSTEN

```java
public static final int LIGHT_SOURCE_TUNGSTEN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_FLASH

```java
public static final int LIGHT_SOURCE_FLASH
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_FINE_WEATHER

```java
public static final int LIGHT_SOURCE_FINE_WEATHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_CLOUDY_WEATHER

```java
public static final int LIGHT_SOURCE_CLOUDY_WEATHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_SHADE

```java
public static final int LIGHT_SOURCE_SHADE
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

```java
public static final int LIGHT_SOURCE_DAYLIGHT_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_DAY_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_COOL_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_STANDARD_LIGHT_A

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_A
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_STANDARD_LIGHT_B

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_B
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_STANDARD_LIGHT_C

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_C
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D55

```java
public static final int LIGHT_SOURCE_D55
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D65

```java
public static final int LIGHT_SOURCE_D65
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D75

```java
public static final int LIGHT_SOURCE_D75
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_D50

```java
public static final int LIGHT_SOURCE_D50
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

```java
public static final int LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- LIGHT_SOURCE_OTHER

```java
public static final int LIGHT_SOURCE_OTHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

- TAG_FLASH

```java
public static final int TAG_FLASH
```

A tag indicating the flash firing status and flash return
status (type SHORT).

**See Also:** FLASH_DID_NOT_FIRE

,

FLASH_FIRED

,

FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

,

FLASH_STROBE_RETURN_LIGHT_DETECTED

,

Constant Field Values

- FLASH_DID_NOT_FIRE

```java
public static final int FLASH_DID_NOT_FIRE
```

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_FIRED

```java
public static final int FLASH_FIRED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

```java
public static final int FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_STROBE_RETURN_LIGHT_DETECTED

```java
public static final int FLASH_STROBE_RETURN_LIGHT_DETECTED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_FIRED

```java
public static final int FLASH_MASK_FIRED
```

A mask to be used with the "Flash" tag, indicating that the
flash fired.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_RETURN_NOT_DETECTED

```java
public static final int FLASH_MASK_RETURN_NOT_DETECTED
```

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_RETURN_DETECTED

```java
public static final int FLASH_MASK_RETURN_DETECTED
```

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_MODE_FLASH_FIRING

```java
public static final int FLASH_MASK_MODE_FLASH_FIRING
```

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_MODE_FLASH_SUPPRESSION

```java
public static final int FLASH_MASK_MODE_FLASH_SUPPRESSION
```

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_MODE_AUTO

```java
public static final int FLASH_MASK_MODE_AUTO
```

A mask to be used with the "Flash" tag, indicating auto mode.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_FUNCTION_NOT_PRESENT

```java
public static final int FLASH_MASK_FUNCTION_NOT_PRESENT
```

A mask to be used with the "Flash" tag, indicating no flash function
present.

**See Also:** TAG_FLASH

,

Constant Field Values

- FLASH_MASK_RED_EYE_REDUCTION

```java
public static final int FLASH_MASK_RED_EYE_REDUCTION
```

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

**See Also:** TAG_FLASH

,

Constant Field Values

- TAG_FOCAL_LENGTH

```java
public static final int TAG_FOCAL_LENGTH
```

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

**See Also:** Constant Field Values

- TAG_SUBJECT_AREA

```java
public static final int TAG_SUBJECT_AREA
```

A tag indicating the location and area of the main subject in
the overall scene.

**See Also:** Constant Field Values

- TAG_FLASH_ENERGY

```java
public static final int TAG_FLASH_ENERGY
```

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_SPATIAL_FREQUENCY_RESPONSE

```java
public static final int TAG_SPATIAL_FREQUENCY_RESPONSE
```

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

**See Also:** Constant Field Values

- TAG_FOCAL_PLANE_X_RESOLUTION

```java
public static final int TAG_FOCAL_PLANE_X_RESOLUTION
```

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_FOCAL_PLANE_Y_RESOLUTION

```java
public static final int TAG_FOCAL_PLANE_Y_RESOLUTION
```

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_FOCAL_PLANE_RESOLUTION_UNIT

```java
public static final int TAG_FOCAL_PLANE_RESOLUTION_UNIT
```

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

**See Also:** FOCAL_PLANE_RESOLUTION_UNIT_NONE

,

FOCAL_PLANE_RESOLUTION_UNIT_INCH

,

FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

- FOCAL_PLANE_RESOLUTION_UNIT_NONE

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_NONE
```

A value to be used with the "FocalPlaneResolutionUnit" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

- FOCAL_PLANE_RESOLUTION_UNIT_INCH

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_INCH
```

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

- FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER
```

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

- TAG_SUBJECT_LOCATION

```java
public static final int TAG_SUBJECT_LOCATION
```

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

**See Also:** Constant Field Values

- TAG_EXPOSURE_INDEX

```java
public static final int TAG_EXPOSURE_INDEX
```

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

**See Also:** Constant Field Values

- TAG_SENSING_METHOD

```java
public static final int TAG_SENSING_METHOD
```

A tag indicating the sensor type on the camera or input device
(type SHORT).

**See Also:** SENSING_METHOD_NOT_DEFINED

,

SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

,

SENSING_METHOD_TRILINEAR_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

,

Constant Field Values

- SENSING_METHOD_NOT_DEFINED

```java
public static final int SENSING_METHOD_NOT_DEFINED
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

```java
public static final int SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_TRILINEAR_SENSOR

```java
public static final int SENSING_METHOD_TRILINEAR_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

```java
public static final int SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

- TAG_FILE_SOURCE

```java
public static final int TAG_FILE_SOURCE
```

A tag indicating the image source (type UNDEFINED).

**See Also:** FILE_SOURCE_DSC

,

Constant Field Values

- FILE_SOURCE_DSC

```java
public static final int FILE_SOURCE_DSC
```

A value to be used with the "FileSource" tag.

**See Also:** TAG_FILE_SOURCE

,

Constant Field Values

- TAG_SCENE_TYPE

```java
public static final int TAG_SCENE_TYPE
```

A tag indicating the type of scene (type UNDEFINED).

**See Also:** SCENE_TYPE_DSC

,

Constant Field Values

- SCENE_TYPE_DSC

```java
public static final int SCENE_TYPE_DSC
```

A value to be used with the "SceneType" tag.

**See Also:** TAG_SCENE_TYPE

,

Constant Field Values

- TAG_CFA_PATTERN

```java
public static final int TAG_CFA_PATTERN
```

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

**See Also:** Constant Field Values

- TAG_CUSTOM_RENDERED

```java
public static final int TAG_CUSTOM_RENDERED
```

A tag indicating the use of special processing on image data,
such as rendering geared to output.

**See Also:** Constant Field Values

- CUSTOM_RENDERED_NORMAL

```java
public static final int CUSTOM_RENDERED_NORMAL
```

A value to be used with the "CustomRendered" tag.

**See Also:** TAG_CUSTOM_RENDERED

,

Constant Field Values

- CUSTOM_RENDERED_CUSTOM

```java
public static final int CUSTOM_RENDERED_CUSTOM
```

A value to be used with the "CustomRendered" tag.

**See Also:** TAG_CUSTOM_RENDERED

,

Constant Field Values

- TAG_EXPOSURE_MODE

```java
public static final int TAG_EXPOSURE_MODE
```

A tag indicating the exposure mode set when the image was shot.

**See Also:** Constant Field Values

- EXPOSURE_MODE_AUTO_EXPOSURE

```java
public static final int EXPOSURE_MODE_AUTO_EXPOSURE
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

- EXPOSURE_MODE_MANUAL_EXPOSURE

```java
public static final int EXPOSURE_MODE_MANUAL_EXPOSURE
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

- EXPOSURE_MODE_AUTO_BRACKET

```java
public static final int EXPOSURE_MODE_AUTO_BRACKET
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

- TAG_WHITE_BALANCE

```java
public static final int TAG_WHITE_BALANCE
```

A tag indicating the white balance mode set when the image was shot.

**See Also:** Constant Field Values

- WHITE_BALANCE_AUTO

```java
public static final int WHITE_BALANCE_AUTO
```

A value to be used with the "WhiteBalance" tag.

**See Also:** TAG_WHITE_BALANCE

,

Constant Field Values

- WHITE_BALANCE_MANUAL

```java
public static final int WHITE_BALANCE_MANUAL
```

A value to be used with the "WhiteBalance" tag.

**See Also:** TAG_WHITE_BALANCE

,

Constant Field Values

- TAG_DIGITAL_ZOOM_RATIO

```java
public static final int TAG_DIGITAL_ZOOM_RATIO
```

A tag indicating the digital zoom ratio when the image was shot.

**See Also:** Constant Field Values

- TAG_FOCAL_LENGTH_IN_35MM_FILM

```java
public static final int TAG_FOCAL_LENGTH_IN_35MM_FILM
```

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

**See Also:** Constant Field Values

- TAG_SCENE_CAPTURE_TYPE

```java
public static final int TAG_SCENE_CAPTURE_TYPE
```

A tag indicating the type of scene that was shot.

**See Also:** Constant Field Values

- SCENE_CAPTURE_TYPE_STANDARD

```java
public static final int SCENE_CAPTURE_TYPE_STANDARD
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- SCENE_CAPTURE_TYPE_LANDSCAPE

```java
public static final int SCENE_CAPTURE_TYPE_LANDSCAPE
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- SCENE_CAPTURE_TYPE_PORTRAIT

```java
public static final int SCENE_CAPTURE_TYPE_PORTRAIT
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- SCENE_CAPTURE_TYPE_NIGHT_SCENE

```java
public static final int SCENE_CAPTURE_TYPE_NIGHT_SCENE
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

- TAG_GAIN_CONTROL

```java
public static final int TAG_GAIN_CONTROL
```

A tag indicating the degree of overall image gain adjustment.

**See Also:** Constant Field Values

- GAIN_CONTROL_NONE

```java
public static final int GAIN_CONTROL_NONE
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_LOW_GAIN_UP

```java
public static final int GAIN_CONTROL_LOW_GAIN_UP
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_HIGH_GAIN_UP

```java
public static final int GAIN_CONTROL_HIGH_GAIN_UP
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_LOW_GAIN_DOWN

```java
public static final int GAIN_CONTROL_LOW_GAIN_DOWN
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- GAIN_CONTROL_HIGH_GAIN_DOWN

```java
public static final int GAIN_CONTROL_HIGH_GAIN_DOWN
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

- TAG_CONTRAST

```java
public static final int TAG_CONTRAST
```

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

**See Also:** Constant Field Values

- CONTRAST_NORMAL

```java
public static final int CONTRAST_NORMAL
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

- CONTRAST_SOFT

```java
public static final int CONTRAST_SOFT
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

- CONTRAST_HARD

```java
public static final int CONTRAST_HARD
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

- TAG_SATURATION

```java
public static final int TAG_SATURATION
```

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

**See Also:** Constant Field Values

- SATURATION_NORMAL

```java
public static final int SATURATION_NORMAL
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

- SATURATION_LOW

```java
public static final int SATURATION_LOW
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

- SATURATION_HIGH

```java
public static final int SATURATION_HIGH
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

- TAG_SHARPNESS

```java
public static final int TAG_SHARPNESS
```

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

**See Also:** Constant Field Values

- SHARPNESS_NORMAL

```java
public static final int SHARPNESS_NORMAL
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

- SHARPNESS_SOFT

```java
public static final int SHARPNESS_SOFT
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

- SHARPNESS_HARD

```java
public static final int SHARPNESS_HARD
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

- TAG_DEVICE_SETTING_DESCRIPTION

```java
public static final int TAG_DEVICE_SETTING_DESCRIPTION
```

A tag indicating information on the picture-taking conditions
of a particular camera model.

**See Also:** Constant Field Values

- TAG_SUBJECT_DISTANCE_RANGE

```java
public static final int TAG_SUBJECT_DISTANCE_RANGE
```

A tag indicating the distance to the subject.

**See Also:** Constant Field Values

- SUBJECT_DISTANCE_RANGE_UNKNOWN

```java
public static final int SUBJECT_DISTANCE_RANGE_UNKNOWN
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- SUBJECT_DISTANCE_RANGE_MACRO

```java
public static final int SUBJECT_DISTANCE_RANGE_MACRO
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

```java
public static final int SUBJECT_DISTANCE_RANGE_CLOSE_VIEW
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

```java
public static final int SUBJECT_DISTANCE_RANGE_DISTANT_VIEW
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

- TAG_IMAGE_UNIQUE_ID

```java
public static final int TAG_IMAGE_UNIQUE_ID
```

A tag indicating an identifier assigned uniquely to each image.

**See Also:** Constant Field Values

---

#### Field Detail

TAG_GPS_INFO_IFD_POINTER

```java
public static final int TAG_GPS_INFO_IFD_POINTER
```

A tag pointing to a GPS info IFD (type LONG). This tag has
been superseded by

ExifParentTIFFTagSet.TAG_GPS_INFO_IFD_POINTER

.

**See Also:** Constant Field Values

---

#### TAG_GPS_INFO_IFD_POINTER

public static final int TAG_GPS_INFO_IFD_POINTER

A tag pointing to a GPS info IFD (type LONG). This tag has
been superseded by

ExifParentTIFFTagSet.TAG_GPS_INFO_IFD_POINTER

.

TAG_INTEROPERABILITY_IFD_POINTER

```java
public static final int TAG_INTEROPERABILITY_IFD_POINTER
```

A tag pointing to an interoperability IFD (type LONG).

**See Also:** Constant Field Values

---

#### TAG_INTEROPERABILITY_IFD_POINTER

public static final int TAG_INTEROPERABILITY_IFD_POINTER

A tag pointing to an interoperability IFD (type LONG).

TAG_EXIF_VERSION

```java
public static final int TAG_EXIF_VERSION
```

A tag containing the Exif version number (type UNDEFINED, count =
4). Conformance to the Exif 2.1 standard is indicated using
the ASCII value "0210" (with no terminating NUL).

**See Also:** EXIF_VERSION_2_1

,

EXIF_VERSION_2_2

,

Constant Field Values

---

#### TAG_EXIF_VERSION

public static final int TAG_EXIF_VERSION

A tag containing the Exif version number (type UNDEFINED, count =
4). Conformance to the Exif 2.1 standard is indicated using
the ASCII value "0210" (with no terminating NUL).

EXIF_VERSION_2_1

```java
public static final
String
EXIF_VERSION_2_1
```

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1. The value equals the US-ASCII encoding of the byte array

{'0', '2', '1', '0'}

.

**See Also:** TAG_EXIF_VERSION

,

Constant Field Values

---

#### EXIF_VERSION_2_1

public static final

String

EXIF_VERSION_2_1

A value to be used with the "ExifVersion" tag to indicate Exif version
2.1. The value equals the US-ASCII encoding of the byte array

{'0', '2', '1', '0'}

.

EXIF_VERSION_2_2

```java
public static final
String
EXIF_VERSION_2_2
```

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2. The value equals the US-ASCII encoding of the byte array

{'0', '2', '2', '0'}

.

**See Also:** TAG_EXIF_VERSION

,

Constant Field Values

---

#### EXIF_VERSION_2_2

public static final

String

EXIF_VERSION_2_2

A value to be used with the "ExifVersion" tag to indicate Exif version
2.2. The value equals the US-ASCII encoding of the byte array

{'0', '2', '2', '0'}

.

TAG_FLASHPIX_VERSION

```java
public static final int TAG_FLASHPIX_VERSION
```

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

**See Also:** Constant Field Values

---

#### TAG_FLASHPIX_VERSION

public static final int TAG_FLASHPIX_VERSION

A tag indicating the FlashPix version number (type UNDEFINED,
count = 4).

TAG_COLOR_SPACE

```java
public static final int TAG_COLOR_SPACE
```

A tag indicating the color space information (type SHORT). The
legal values are given by the

COLOR_SPACE_*

constants.

**See Also:** COLOR_SPACE_SRGB

,

COLOR_SPACE_UNCALIBRATED

,

Constant Field Values

---

#### TAG_COLOR_SPACE

public static final int TAG_COLOR_SPACE

A tag indicating the color space information (type SHORT). The
legal values are given by the

COLOR_SPACE_*

constants.

COLOR_SPACE_SRGB

```java
public static final int COLOR_SPACE_SRGB
```

A value to be used with the "ColorSpace" tag.

**See Also:** TAG_COLOR_SPACE

,

Constant Field Values

---

#### COLOR_SPACE_SRGB

public static final int COLOR_SPACE_SRGB

A value to be used with the "ColorSpace" tag.

COLOR_SPACE_UNCALIBRATED

```java
public static final int COLOR_SPACE_UNCALIBRATED
```

A value to be used with the "ColorSpace" tag.

**See Also:** TAG_COLOR_SPACE

,

Constant Field Values

---

#### COLOR_SPACE_UNCALIBRATED

public static final int COLOR_SPACE_UNCALIBRATED

A value to be used with the "ColorSpace" tag.

TAG_COMPONENTS_CONFIGURATION

```java
public static final int TAG_COMPONENTS_CONFIGURATION
```

A tag containing the components configuration information (type
UNDEFINED, count = 4).

**See Also:** COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

,

COMPONENTS_CONFIGURATION_Y

,

COMPONENTS_CONFIGURATION_CB

,

COMPONENTS_CONFIGURATION_CR

,

COMPONENTS_CONFIGURATION_R

,

COMPONENTS_CONFIGURATION_G

,

COMPONENTS_CONFIGURATION_B

,

Constant Field Values

---

#### TAG_COMPONENTS_CONFIGURATION

public static final int TAG_COMPONENTS_CONFIGURATION

A tag containing the components configuration information (type
UNDEFINED, count = 4).

COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

```java
public static final int COMPONENTS_CONFIGURATION_DOES_NOT_EXIST
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

public static final int COMPONENTS_CONFIGURATION_DOES_NOT_EXIST

A value to be used with the "ComponentsConfiguration" tag.

COMPONENTS_CONFIGURATION_Y

```java
public static final int COMPONENTS_CONFIGURATION_Y
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### COMPONENTS_CONFIGURATION_Y

public static final int COMPONENTS_CONFIGURATION_Y

A value to be used with the "ComponentsConfiguration" tag.

COMPONENTS_CONFIGURATION_CB

```java
public static final int COMPONENTS_CONFIGURATION_CB
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### COMPONENTS_CONFIGURATION_CB

public static final int COMPONENTS_CONFIGURATION_CB

A value to be used with the "ComponentsConfiguration" tag.

COMPONENTS_CONFIGURATION_CR

```java
public static final int COMPONENTS_CONFIGURATION_CR
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### COMPONENTS_CONFIGURATION_CR

public static final int COMPONENTS_CONFIGURATION_CR

A value to be used with the "ComponentsConfiguration" tag.

COMPONENTS_CONFIGURATION_R

```java
public static final int COMPONENTS_CONFIGURATION_R
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### COMPONENTS_CONFIGURATION_R

public static final int COMPONENTS_CONFIGURATION_R

A value to be used with the "ComponentsConfiguration" tag.

COMPONENTS_CONFIGURATION_G

```java
public static final int COMPONENTS_CONFIGURATION_G
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### COMPONENTS_CONFIGURATION_G

public static final int COMPONENTS_CONFIGURATION_G

A value to be used with the "ComponentsConfiguration" tag.

COMPONENTS_CONFIGURATION_B

```java
public static final int COMPONENTS_CONFIGURATION_B
```

A value to be used with the "ComponentsConfiguration" tag.

**See Also:** TAG_COMPONENTS_CONFIGURATION

,

Constant Field Values

---

#### COMPONENTS_CONFIGURATION_B

public static final int COMPONENTS_CONFIGURATION_B

A value to be used with the "ComponentsConfiguration" tag.

TAG_COMPRESSED_BITS_PER_PIXEL

```java
public static final int TAG_COMPRESSED_BITS_PER_PIXEL
```

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_COMPRESSED_BITS_PER_PIXEL

public static final int TAG_COMPRESSED_BITS_PER_PIXEL

A tag indicating the number of compressed bits per pixel
(type RATIONAL).

TAG_PIXEL_X_DIMENSION

```java
public static final int TAG_PIXEL_X_DIMENSION
```

A tag indicating the pixel X dimension (type SHORT or LONG).
This value records the valid width of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:** Constant Field Values

---

#### TAG_PIXEL_X_DIMENSION

public static final int TAG_PIXEL_X_DIMENSION

A tag indicating the pixel X dimension (type SHORT or LONG).
This value records the valid width of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

TAG_PIXEL_Y_DIMENSION

```java
public static final int TAG_PIXEL_Y_DIMENSION
```

A tag indicating the pixel Y dimension (type SHORT or LONG).
This value records the valid height of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

**See Also:** Constant Field Values

---

#### TAG_PIXEL_Y_DIMENSION

public static final int TAG_PIXEL_Y_DIMENSION

A tag indicating the pixel Y dimension (type SHORT or LONG).
This value records the valid height of the meaningful image for
a compressed file, whether or not there is padding or a restart
marker.

TAG_MAKER_NOTE

```java
public static final int TAG_MAKER_NOTE
```

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

**See Also:** Constant Field Values

---

#### TAG_MAKER_NOTE

public static final int TAG_MAKER_NOTE

A tag indicating a manufacturer-defined maker note (type
UNDEFINED).

TAG_MARKER_NOTE

```java
public static final int TAG_MARKER_NOTE
```

A tag indicating a manufacturer-defined marker note (type UNDEFINED).
This tag has been superseded by

TAG_MAKER_NOTE

.

**See Also:** Constant Field Values

---

#### TAG_MARKER_NOTE

public static final int TAG_MARKER_NOTE

A tag indicating a manufacturer-defined marker note (type UNDEFINED).
This tag has been superseded by

TAG_MAKER_NOTE

.

TAG_USER_COMMENT

```java
public static final int TAG_USER_COMMENT
```

A tag indicating a user comment (type UNDEFINED). The first 8
bytes are used to specify the character encoding.

**See Also:** Constant Field Values

---

#### TAG_USER_COMMENT

public static final int TAG_USER_COMMENT

A tag indicating a user comment (type UNDEFINED). The first 8
bytes are used to specify the character encoding.

TAG_RELATED_SOUND_FILE

```java
public static final int TAG_RELATED_SOUND_FILE
```

A tag indicating the name of a related sound file (type ASCII).

**See Also:** Constant Field Values

---

#### TAG_RELATED_SOUND_FILE

public static final int TAG_RELATED_SOUND_FILE

A tag indicating the name of a related sound file (type ASCII).

TAG_DATE_TIME_ORIGINAL

```java
public static final int TAG_DATE_TIME_ORIGINAL
```

A tag indicating the date and time when the original image was
generated (type ASCII).

**See Also:** Constant Field Values

---

#### TAG_DATE_TIME_ORIGINAL

public static final int TAG_DATE_TIME_ORIGINAL

A tag indicating the date and time when the original image was
generated (type ASCII).

TAG_DATE_TIME_DIGITIZED

```java
public static final int TAG_DATE_TIME_DIGITIZED
```

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

**See Also:** Constant Field Values

---

#### TAG_DATE_TIME_DIGITIZED

public static final int TAG_DATE_TIME_DIGITIZED

A tag indicating the date and time when the image was stored as
digital data (type ASCII).

TAG_SUB_SEC_TIME

```java
public static final int TAG_SUB_SEC_TIME
```

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

**See Also:** Constant Field Values

---

#### TAG_SUB_SEC_TIME

public static final int TAG_SUB_SEC_TIME

A tag used to record fractions of seconds for the "DateTime" tag
(type ASCII).

TAG_SUB_SEC_TIME_ORIGINAL

```java
public static final int TAG_SUB_SEC_TIME_ORIGINAL
```

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

**See Also:** Constant Field Values

---

#### TAG_SUB_SEC_TIME_ORIGINAL

public static final int TAG_SUB_SEC_TIME_ORIGINAL

A tag used to record fractions of seconds for the
"DateTimeOriginal" tag (type ASCII).

TAG_SUB_SEC_TIME_DIGITIZED

```java
public static final int TAG_SUB_SEC_TIME_DIGITIZED
```

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

**See Also:** Constant Field Values

---

#### TAG_SUB_SEC_TIME_DIGITIZED

public static final int TAG_SUB_SEC_TIME_DIGITIZED

A tag used to record fractions of seconds for the
"DateTimeDigitized" tag (type ASCII).

TAG_EXPOSURE_TIME

```java
public static final int TAG_EXPOSURE_TIME
```

A tag indicating the exposure time, in seconds (type RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_EXPOSURE_TIME

public static final int TAG_EXPOSURE_TIME

A tag indicating the exposure time, in seconds (type RATIONAL).

TAG_F_NUMBER

```java
public static final int TAG_F_NUMBER
```

A tag indicating the F number (type RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_F_NUMBER

public static final int TAG_F_NUMBER

A tag indicating the F number (type RATIONAL).

TAG_EXPOSURE_PROGRAM

```java
public static final int TAG_EXPOSURE_PROGRAM
```

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

**See Also:** EXPOSURE_PROGRAM_NOT_DEFINED

,

EXPOSURE_PROGRAM_MANUAL

,

EXPOSURE_PROGRAM_NORMAL_PROGRAM

,

EXPOSURE_PROGRAM_APERTURE_PRIORITY

,

EXPOSURE_PROGRAM_SHUTTER_PRIORITY

,

EXPOSURE_PROGRAM_CREATIVE_PROGRAM

,

EXPOSURE_PROGRAM_ACTION_PROGRAM

,

EXPOSURE_PROGRAM_PORTRAIT_MODE

,

EXPOSURE_PROGRAM_LANDSCAPE_MODE

,

EXPOSURE_PROGRAM_MAX_RESERVED

,

Constant Field Values

---

#### TAG_EXPOSURE_PROGRAM

public static final int TAG_EXPOSURE_PROGRAM

A tag indicating the class of the programs used to set exposure
when the picture was taken (type SHORT).

EXPOSURE_PROGRAM_NOT_DEFINED

```java
public static final int EXPOSURE_PROGRAM_NOT_DEFINED
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_NOT_DEFINED

public static final int EXPOSURE_PROGRAM_NOT_DEFINED

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_MANUAL

```java
public static final int EXPOSURE_PROGRAM_MANUAL
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_MANUAL

public static final int EXPOSURE_PROGRAM_MANUAL

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_NORMAL_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_NORMAL_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_NORMAL_PROGRAM

public static final int EXPOSURE_PROGRAM_NORMAL_PROGRAM

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_APERTURE_PRIORITY

```java
public static final int EXPOSURE_PROGRAM_APERTURE_PRIORITY
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_APERTURE_PRIORITY

public static final int EXPOSURE_PROGRAM_APERTURE_PRIORITY

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_SHUTTER_PRIORITY

```java
public static final int EXPOSURE_PROGRAM_SHUTTER_PRIORITY
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_SHUTTER_PRIORITY

public static final int EXPOSURE_PROGRAM_SHUTTER_PRIORITY

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_CREATIVE_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_CREATIVE_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_CREATIVE_PROGRAM

public static final int EXPOSURE_PROGRAM_CREATIVE_PROGRAM

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_ACTION_PROGRAM

```java
public static final int EXPOSURE_PROGRAM_ACTION_PROGRAM
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_ACTION_PROGRAM

public static final int EXPOSURE_PROGRAM_ACTION_PROGRAM

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_PORTRAIT_MODE

```java
public static final int EXPOSURE_PROGRAM_PORTRAIT_MODE
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_PORTRAIT_MODE

public static final int EXPOSURE_PROGRAM_PORTRAIT_MODE

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_LANDSCAPE_MODE

```java
public static final int EXPOSURE_PROGRAM_LANDSCAPE_MODE
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_LANDSCAPE_MODE

public static final int EXPOSURE_PROGRAM_LANDSCAPE_MODE

A value to be used with the "ExposureProgram" tag.

EXPOSURE_PROGRAM_MAX_RESERVED

```java
public static final int EXPOSURE_PROGRAM_MAX_RESERVED
```

A value to be used with the "ExposureProgram" tag.

**See Also:** TAG_EXPOSURE_PROGRAM

,

Constant Field Values

---

#### EXPOSURE_PROGRAM_MAX_RESERVED

public static final int EXPOSURE_PROGRAM_MAX_RESERVED

A value to be used with the "ExposureProgram" tag.

TAG_SPECTRAL_SENSITIVITY

```java
public static final int TAG_SPECTRAL_SENSITIVITY
```

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII). The tag value is an ASCII string
compatible with the ASTM standard.

**See Also:** Constant Field Values

---

#### TAG_SPECTRAL_SENSITIVITY

public static final int TAG_SPECTRAL_SENSITIVITY

A tag indicating the spectral sensitivity of each channel of
the camera used (type ASCII). The tag value is an ASCII string
compatible with the ASTM standard.

TAG_ISO_SPEED_RATINGS

```java
public static final int TAG_ISO_SPEED_RATINGS
```

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

**See Also:** Constant Field Values

---

#### TAG_ISO_SPEED_RATINGS

public static final int TAG_ISO_SPEED_RATINGS

A tag indicating the ISO speed and ISO latitude of the camera
or input device, as specified in ISO 12232

xiv

(type
SHORT).

TAG_OECF

```java
public static final int TAG_OECF
```

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED). OECF is
the relationship between the camera optical input and the image
values.

**See Also:** Constant Field Values

---

#### TAG_OECF

public static final int TAG_OECF

A tag indicating the optoelectric conversion function,
specified in ISO 14254

xv

(type UNDEFINED). OECF is
the relationship between the camera optical input and the image
values.

TAG_SHUTTER_SPEED_VALUE

```java
public static final int TAG_SHUTTER_SPEED_VALUE
```

A tag indicating the shutter speed (type SRATIONAL).

**See Also:** Constant Field Values

---

#### TAG_SHUTTER_SPEED_VALUE

public static final int TAG_SHUTTER_SPEED_VALUE

A tag indicating the shutter speed (type SRATIONAL).

TAG_APERTURE_VALUE

```java
public static final int TAG_APERTURE_VALUE
```

A tag indicating the lens aperture (type RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_APERTURE_VALUE

public static final int TAG_APERTURE_VALUE

A tag indicating the lens aperture (type RATIONAL).

TAG_BRIGHTNESS_VALUE

```java
public static final int TAG_BRIGHTNESS_VALUE
```

A tag indicating the value of brightness (type SRATIONAL).

**See Also:** Constant Field Values

---

#### TAG_BRIGHTNESS_VALUE

public static final int TAG_BRIGHTNESS_VALUE

A tag indicating the value of brightness (type SRATIONAL).

TAG_EXPOSURE_BIAS_VALUE

```java
public static final int TAG_EXPOSURE_BIAS_VALUE
```

A tag indicating the exposure bias (type SRATIONAL).

**See Also:** Constant Field Values

---

#### TAG_EXPOSURE_BIAS_VALUE

public static final int TAG_EXPOSURE_BIAS_VALUE

A tag indicating the exposure bias (type SRATIONAL).

TAG_MAX_APERTURE_VALUE

```java
public static final int TAG_MAX_APERTURE_VALUE
```

A tag indicating the smallest F number of the lens (type
RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_MAX_APERTURE_VALUE

public static final int TAG_MAX_APERTURE_VALUE

A tag indicating the smallest F number of the lens (type
RATIONAL).

TAG_SUBJECT_DISTANCE

```java
public static final int TAG_SUBJECT_DISTANCE
```

A tag indicating the distance to the subject, in meters (type
RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_SUBJECT_DISTANCE

public static final int TAG_SUBJECT_DISTANCE

A tag indicating the distance to the subject, in meters (type
RATIONAL).

TAG_METERING_MODE

```java
public static final int TAG_METERING_MODE
```

A tag indicating the metering mode (type SHORT).

**See Also:** METERING_MODE_UNKNOWN

,

METERING_MODE_AVERAGE

,

METERING_MODE_CENTER_WEIGHTED_AVERAGE

,

METERING_MODE_SPOT

,

METERING_MODE_MULTI_SPOT

,

METERING_MODE_PATTERN

,

METERING_MODE_PARTIAL

,

METERING_MODE_MIN_RESERVED

,

METERING_MODE_MAX_RESERVED

,

METERING_MODE_OTHER

,

Constant Field Values

---

#### TAG_METERING_MODE

public static final int TAG_METERING_MODE

A tag indicating the metering mode (type SHORT).

METERING_MODE_UNKNOWN

```java
public static final int METERING_MODE_UNKNOWN
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_UNKNOWN

public static final int METERING_MODE_UNKNOWN

A value to be used with the "MeteringMode" tag.

METERING_MODE_AVERAGE

```java
public static final int METERING_MODE_AVERAGE
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_AVERAGE

public static final int METERING_MODE_AVERAGE

A value to be used with the "MeteringMode" tag.

METERING_MODE_CENTER_WEIGHTED_AVERAGE

```java
public static final int METERING_MODE_CENTER_WEIGHTED_AVERAGE
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_CENTER_WEIGHTED_AVERAGE

public static final int METERING_MODE_CENTER_WEIGHTED_AVERAGE

A value to be used with the "MeteringMode" tag.

METERING_MODE_SPOT

```java
public static final int METERING_MODE_SPOT
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_SPOT

public static final int METERING_MODE_SPOT

A value to be used with the "MeteringMode" tag.

METERING_MODE_MULTI_SPOT

```java
public static final int METERING_MODE_MULTI_SPOT
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_MULTI_SPOT

public static final int METERING_MODE_MULTI_SPOT

A value to be used with the "MeteringMode" tag.

METERING_MODE_PATTERN

```java
public static final int METERING_MODE_PATTERN
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_PATTERN

public static final int METERING_MODE_PATTERN

A value to be used with the "MeteringMode" tag.

METERING_MODE_PARTIAL

```java
public static final int METERING_MODE_PARTIAL
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_PARTIAL

public static final int METERING_MODE_PARTIAL

A value to be used with the "MeteringMode" tag.

METERING_MODE_MIN_RESERVED

```java
public static final int METERING_MODE_MIN_RESERVED
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_MIN_RESERVED

public static final int METERING_MODE_MIN_RESERVED

A value to be used with the "MeteringMode" tag.

METERING_MODE_MAX_RESERVED

```java
public static final int METERING_MODE_MAX_RESERVED
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_MAX_RESERVED

public static final int METERING_MODE_MAX_RESERVED

A value to be used with the "MeteringMode" tag.

METERING_MODE_OTHER

```java
public static final int METERING_MODE_OTHER
```

A value to be used with the "MeteringMode" tag.

**See Also:** TAG_METERING_MODE

,

Constant Field Values

---

#### METERING_MODE_OTHER

public static final int METERING_MODE_OTHER

A value to be used with the "MeteringMode" tag.

TAG_LIGHT_SOURCE

```java
public static final int TAG_LIGHT_SOURCE
```

A tag indicatingthe kind of light source (type SHORT).

**See Also:** LIGHT_SOURCE_UNKNOWN

,

LIGHT_SOURCE_DAYLIGHT

,

LIGHT_SOURCE_FLUORESCENT

,

LIGHT_SOURCE_TUNGSTEN

,

LIGHT_SOURCE_STANDARD_LIGHT_A

,

LIGHT_SOURCE_STANDARD_LIGHT_B

,

LIGHT_SOURCE_STANDARD_LIGHT_C

,

LIGHT_SOURCE_D55

,

LIGHT_SOURCE_D65

,

LIGHT_SOURCE_D75

,

LIGHT_SOURCE_OTHER

,

Constant Field Values

---

#### TAG_LIGHT_SOURCE

public static final int TAG_LIGHT_SOURCE

A tag indicatingthe kind of light source (type SHORT).

LIGHT_SOURCE_UNKNOWN

```java
public static final int LIGHT_SOURCE_UNKNOWN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_UNKNOWN

public static final int LIGHT_SOURCE_UNKNOWN

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_DAYLIGHT

```java
public static final int LIGHT_SOURCE_DAYLIGHT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_DAYLIGHT

public static final int LIGHT_SOURCE_DAYLIGHT

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_FLUORESCENT

public static final int LIGHT_SOURCE_FLUORESCENT

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_TUNGSTEN

```java
public static final int LIGHT_SOURCE_TUNGSTEN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_TUNGSTEN

public static final int LIGHT_SOURCE_TUNGSTEN

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_FLASH

```java
public static final int LIGHT_SOURCE_FLASH
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_FLASH

public static final int LIGHT_SOURCE_FLASH

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_FINE_WEATHER

```java
public static final int LIGHT_SOURCE_FINE_WEATHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_FINE_WEATHER

public static final int LIGHT_SOURCE_FINE_WEATHER

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_CLOUDY_WEATHER

```java
public static final int LIGHT_SOURCE_CLOUDY_WEATHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_CLOUDY_WEATHER

public static final int LIGHT_SOURCE_CLOUDY_WEATHER

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_SHADE

```java
public static final int LIGHT_SOURCE_SHADE
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_SHADE

public static final int LIGHT_SOURCE_SHADE

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

```java
public static final int LIGHT_SOURCE_DAYLIGHT_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

public static final int LIGHT_SOURCE_DAYLIGHT_FLUORESCENT

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_DAY_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

public static final int LIGHT_SOURCE_DAY_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_COOL_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

public static final int LIGHT_SOURCE_COOL_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_WHITE_FLUORESCENT

```java
public static final int LIGHT_SOURCE_WHITE_FLUORESCENT
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_WHITE_FLUORESCENT

public static final int LIGHT_SOURCE_WHITE_FLUORESCENT

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_STANDARD_LIGHT_A

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_A
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_STANDARD_LIGHT_A

public static final int LIGHT_SOURCE_STANDARD_LIGHT_A

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_STANDARD_LIGHT_B

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_B
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_STANDARD_LIGHT_B

public static final int LIGHT_SOURCE_STANDARD_LIGHT_B

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_STANDARD_LIGHT_C

```java
public static final int LIGHT_SOURCE_STANDARD_LIGHT_C
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_STANDARD_LIGHT_C

public static final int LIGHT_SOURCE_STANDARD_LIGHT_C

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_D55

```java
public static final int LIGHT_SOURCE_D55
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_D55

public static final int LIGHT_SOURCE_D55

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_D65

```java
public static final int LIGHT_SOURCE_D65
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_D65

public static final int LIGHT_SOURCE_D65

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_D75

```java
public static final int LIGHT_SOURCE_D75
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_D75

public static final int LIGHT_SOURCE_D75

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_D50

```java
public static final int LIGHT_SOURCE_D50
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_D50

public static final int LIGHT_SOURCE_D50

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

```java
public static final int LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

public static final int LIGHT_SOURCE_ISO_STUDIO_TUNGSTEN

A value to be used with the "LightSource" tag.

LIGHT_SOURCE_OTHER

```java
public static final int LIGHT_SOURCE_OTHER
```

A value to be used with the "LightSource" tag.

**See Also:** TAG_LIGHT_SOURCE

,

Constant Field Values

---

#### LIGHT_SOURCE_OTHER

public static final int LIGHT_SOURCE_OTHER

A value to be used with the "LightSource" tag.

TAG_FLASH

```java
public static final int TAG_FLASH
```

A tag indicating the flash firing status and flash return
status (type SHORT).

**See Also:** FLASH_DID_NOT_FIRE

,

FLASH_FIRED

,

FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

,

FLASH_STROBE_RETURN_LIGHT_DETECTED

,

Constant Field Values

---

#### TAG_FLASH

public static final int TAG_FLASH

A tag indicating the flash firing status and flash return
status (type SHORT).

FLASH_DID_NOT_FIRE

```java
public static final int FLASH_DID_NOT_FIRE
```

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_DID_NOT_FIRE

public static final int FLASH_DID_NOT_FIRE

A value to be used with the "Flash" tag, indicating that the
flash did not fire.

FLASH_FIRED

```java
public static final int FLASH_FIRED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_FIRED

public static final int FLASH_FIRED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return status is unknown.

FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

```java
public static final int FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

public static final int FLASH_STROBE_RETURN_LIGHT_NOT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, but the strobe return light was not detected.

FLASH_STROBE_RETURN_LIGHT_DETECTED

```java
public static final int FLASH_STROBE_RETURN_LIGHT_DETECTED
```

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_STROBE_RETURN_LIGHT_DETECTED

public static final int FLASH_STROBE_RETURN_LIGHT_DETECTED

A value to be used with the "Flash" tag, indicating that the
flash fired, and the strobe return light was detected.

FLASH_MASK_FIRED

```java
public static final int FLASH_MASK_FIRED
```

A mask to be used with the "Flash" tag, indicating that the
flash fired.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_FIRED

public static final int FLASH_MASK_FIRED

A mask to be used with the "Flash" tag, indicating that the
flash fired.

FLASH_MASK_RETURN_NOT_DETECTED

```java
public static final int FLASH_MASK_RETURN_NOT_DETECTED
```

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_RETURN_NOT_DETECTED

public static final int FLASH_MASK_RETURN_NOT_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light not detected.

FLASH_MASK_RETURN_DETECTED

```java
public static final int FLASH_MASK_RETURN_DETECTED
```

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_RETURN_DETECTED

public static final int FLASH_MASK_RETURN_DETECTED

A mask to be used with the "Flash" tag, indicating strobe return
light detected.

FLASH_MASK_MODE_FLASH_FIRING

```java
public static final int FLASH_MASK_MODE_FLASH_FIRING
```

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_MODE_FLASH_FIRING

public static final int FLASH_MASK_MODE_FLASH_FIRING

A mask to be used with the "Flash" tag, indicating compulsory flash
firing mode.

FLASH_MASK_MODE_FLASH_SUPPRESSION

```java
public static final int FLASH_MASK_MODE_FLASH_SUPPRESSION
```

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_MODE_FLASH_SUPPRESSION

public static final int FLASH_MASK_MODE_FLASH_SUPPRESSION

A mask to be used with the "Flash" tag, indicating compulsory flash
suppression mode.

FLASH_MASK_MODE_AUTO

```java
public static final int FLASH_MASK_MODE_AUTO
```

A mask to be used with the "Flash" tag, indicating auto mode.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_MODE_AUTO

public static final int FLASH_MASK_MODE_AUTO

A mask to be used with the "Flash" tag, indicating auto mode.

FLASH_MASK_FUNCTION_NOT_PRESENT

```java
public static final int FLASH_MASK_FUNCTION_NOT_PRESENT
```

A mask to be used with the "Flash" tag, indicating no flash function
present.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_FUNCTION_NOT_PRESENT

public static final int FLASH_MASK_FUNCTION_NOT_PRESENT

A mask to be used with the "Flash" tag, indicating no flash function
present.

FLASH_MASK_RED_EYE_REDUCTION

```java
public static final int FLASH_MASK_RED_EYE_REDUCTION
```

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

**See Also:** TAG_FLASH

,

Constant Field Values

---

#### FLASH_MASK_RED_EYE_REDUCTION

public static final int FLASH_MASK_RED_EYE_REDUCTION

A mask to be used with the "Flash" tag, indicating red-eye reduction
supported.

TAG_FOCAL_LENGTH

```java
public static final int TAG_FOCAL_LENGTH
```

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_FOCAL_LENGTH

public static final int TAG_FOCAL_LENGTH

A tag indicating the actual focal length of the lens, in
millimeters (type RATIONAL).

TAG_SUBJECT_AREA

```java
public static final int TAG_SUBJECT_AREA
```

A tag indicating the location and area of the main subject in
the overall scene.

**See Also:** Constant Field Values

---

#### TAG_SUBJECT_AREA

public static final int TAG_SUBJECT_AREA

A tag indicating the location and area of the main subject in
the overall scene.

TAG_FLASH_ENERGY

```java
public static final int TAG_FLASH_ENERGY
```

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_FLASH_ENERGY

public static final int TAG_FLASH_ENERGY

A tag indicating the strobe energy at the time the image was
captured, as measured in Beam Candle Power Seconds (BCPS) (type
RATIONAL).

TAG_SPATIAL_FREQUENCY_RESPONSE

```java
public static final int TAG_SPATIAL_FREQUENCY_RESPONSE
```

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

**See Also:** Constant Field Values

---

#### TAG_SPATIAL_FREQUENCY_RESPONSE

public static final int TAG_SPATIAL_FREQUENCY_RESPONSE

A tag indicating the camera or input device spatial frequency
table and SFR values in the direction of image width, image
height, and diagonal direction, as specified in ISO
12233

xvi

(type UNDEFINED).

TAG_FOCAL_PLANE_X_RESOLUTION

```java
public static final int TAG_FOCAL_PLANE_X_RESOLUTION
```

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_FOCAL_PLANE_X_RESOLUTION

public static final int TAG_FOCAL_PLANE_X_RESOLUTION

Indicates the number of pixels in the image width (X) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

TAG_FOCAL_PLANE_Y_RESOLUTION

```java
public static final int TAG_FOCAL_PLANE_Y_RESOLUTION
```

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_FOCAL_PLANE_Y_RESOLUTION

public static final int TAG_FOCAL_PLANE_Y_RESOLUTION

Indicate the number of pixels in the image height (Y) direction
per FocalPlaneResolutionUnit on the camera focal plane (type
RATIONAL).

TAG_FOCAL_PLANE_RESOLUTION_UNIT

```java
public static final int TAG_FOCAL_PLANE_RESOLUTION_UNIT
```

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

**See Also:** FOCAL_PLANE_RESOLUTION_UNIT_NONE

,

FOCAL_PLANE_RESOLUTION_UNIT_INCH

,

FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

,

Constant Field Values

---

#### TAG_FOCAL_PLANE_RESOLUTION_UNIT

public static final int TAG_FOCAL_PLANE_RESOLUTION_UNIT

Indicates the unit for measuring FocalPlaneXResolution and
FocalPlaneYResolution (type SHORT).

FOCAL_PLANE_RESOLUTION_UNIT_NONE

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_NONE
```

A value to be used with the "FocalPlaneResolutionUnit" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

---

#### FOCAL_PLANE_RESOLUTION_UNIT_NONE

public static final int FOCAL_PLANE_RESOLUTION_UNIT_NONE

A value to be used with the "FocalPlaneResolutionUnit" tag.

FOCAL_PLANE_RESOLUTION_UNIT_INCH

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_INCH
```

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

---

#### FOCAL_PLANE_RESOLUTION_UNIT_INCH

public static final int FOCAL_PLANE_RESOLUTION_UNIT_INCH

A value to be used with the "FocalPlaneXResolution" tag.

FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

```java
public static final int FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER
```

A value to be used with the "FocalPlaneXResolution" tag.

**See Also:** TAG_FOCAL_PLANE_RESOLUTION_UNIT

,

Constant Field Values

---

#### FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

public static final int FOCAL_PLANE_RESOLUTION_UNIT_CENTIMETER

A value to be used with the "FocalPlaneXResolution" tag.

TAG_SUBJECT_LOCATION

```java
public static final int TAG_SUBJECT_LOCATION
```

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

**See Also:** Constant Field Values

---

#### TAG_SUBJECT_LOCATION

public static final int TAG_SUBJECT_LOCATION

A tag indicating the column and row of the center pixel of the
main subject in the scene (type SHORT, count = 2).

TAG_EXPOSURE_INDEX

```java
public static final int TAG_EXPOSURE_INDEX
```

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

**See Also:** Constant Field Values

---

#### TAG_EXPOSURE_INDEX

public static final int TAG_EXPOSURE_INDEX

A tag indicating the exposure index selected on the camera or
input device at the time the image was captured (type
RATIONAL).

TAG_SENSING_METHOD

```java
public static final int TAG_SENSING_METHOD
```

A tag indicating the sensor type on the camera or input device
(type SHORT).

**See Also:** SENSING_METHOD_NOT_DEFINED

,

SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

,

SENSING_METHOD_TRILINEAR_SENSOR

,

SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

,

Constant Field Values

---

#### TAG_SENSING_METHOD

public static final int TAG_SENSING_METHOD

A tag indicating the sensor type on the camera or input device
(type SHORT).

SENSING_METHOD_NOT_DEFINED

```java
public static final int SENSING_METHOD_NOT_DEFINED
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

---

#### SENSING_METHOD_NOT_DEFINED

public static final int SENSING_METHOD_NOT_DEFINED

A value to be used with the "SensingMethod" tag.

SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

---

#### SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

public static final int SENSING_METHOD_ONE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

---

#### SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

public static final int SENSING_METHOD_TWO_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

```java
public static final int SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

---

#### SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

public static final int SENSING_METHOD_THREE_CHIP_COLOR_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

```java
public static final int SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

---

#### SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

public static final int SENSING_METHOD_COLOR_SEQUENTIAL_AREA_SENSOR

A value to be used with the "SensingMethod" tag.

SENSING_METHOD_TRILINEAR_SENSOR

```java
public static final int SENSING_METHOD_TRILINEAR_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

---

#### SENSING_METHOD_TRILINEAR_SENSOR

public static final int SENSING_METHOD_TRILINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

```java
public static final int SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR
```

A value to be used with the "SensingMethod" tag.

**See Also:** TAG_SENSING_METHOD

,

Constant Field Values

---

#### SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

public static final int SENSING_METHOD_COLOR_SEQUENTIAL_LINEAR_SENSOR

A value to be used with the "SensingMethod" tag.

TAG_FILE_SOURCE

```java
public static final int TAG_FILE_SOURCE
```

A tag indicating the image source (type UNDEFINED).

**See Also:** FILE_SOURCE_DSC

,

Constant Field Values

---

#### TAG_FILE_SOURCE

public static final int TAG_FILE_SOURCE

A tag indicating the image source (type UNDEFINED).

FILE_SOURCE_DSC

```java
public static final int FILE_SOURCE_DSC
```

A value to be used with the "FileSource" tag.

**See Also:** TAG_FILE_SOURCE

,

Constant Field Values

---

#### FILE_SOURCE_DSC

public static final int FILE_SOURCE_DSC

A value to be used with the "FileSource" tag.

TAG_SCENE_TYPE

```java
public static final int TAG_SCENE_TYPE
```

A tag indicating the type of scene (type UNDEFINED).

**See Also:** SCENE_TYPE_DSC

,

Constant Field Values

---

#### TAG_SCENE_TYPE

public static final int TAG_SCENE_TYPE

A tag indicating the type of scene (type UNDEFINED).

SCENE_TYPE_DSC

```java
public static final int SCENE_TYPE_DSC
```

A value to be used with the "SceneType" tag.

**See Also:** TAG_SCENE_TYPE

,

Constant Field Values

---

#### SCENE_TYPE_DSC

public static final int SCENE_TYPE_DSC

A value to be used with the "SceneType" tag.

TAG_CFA_PATTERN

```java
public static final int TAG_CFA_PATTERN
```

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

**See Also:** Constant Field Values

---

#### TAG_CFA_PATTERN

public static final int TAG_CFA_PATTERN

A tag indicating the color filter array geometric pattern of
the image sensor when a one-chip color area sensor if used
(type UNDEFINED).

TAG_CUSTOM_RENDERED

```java
public static final int TAG_CUSTOM_RENDERED
```

A tag indicating the use of special processing on image data,
such as rendering geared to output.

**See Also:** Constant Field Values

---

#### TAG_CUSTOM_RENDERED

public static final int TAG_CUSTOM_RENDERED

A tag indicating the use of special processing on image data,
such as rendering geared to output.

CUSTOM_RENDERED_NORMAL

```java
public static final int CUSTOM_RENDERED_NORMAL
```

A value to be used with the "CustomRendered" tag.

**See Also:** TAG_CUSTOM_RENDERED

,

Constant Field Values

---

#### CUSTOM_RENDERED_NORMAL

public static final int CUSTOM_RENDERED_NORMAL

A value to be used with the "CustomRendered" tag.

CUSTOM_RENDERED_CUSTOM

```java
public static final int CUSTOM_RENDERED_CUSTOM
```

A value to be used with the "CustomRendered" tag.

**See Also:** TAG_CUSTOM_RENDERED

,

Constant Field Values

---

#### CUSTOM_RENDERED_CUSTOM

public static final int CUSTOM_RENDERED_CUSTOM

A value to be used with the "CustomRendered" tag.

TAG_EXPOSURE_MODE

```java
public static final int TAG_EXPOSURE_MODE
```

A tag indicating the exposure mode set when the image was shot.

**See Also:** Constant Field Values

---

#### TAG_EXPOSURE_MODE

public static final int TAG_EXPOSURE_MODE

A tag indicating the exposure mode set when the image was shot.

EXPOSURE_MODE_AUTO_EXPOSURE

```java
public static final int EXPOSURE_MODE_AUTO_EXPOSURE
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

---

#### EXPOSURE_MODE_AUTO_EXPOSURE

public static final int EXPOSURE_MODE_AUTO_EXPOSURE

A value to be used with the "ExposureMode" tag.

EXPOSURE_MODE_MANUAL_EXPOSURE

```java
public static final int EXPOSURE_MODE_MANUAL_EXPOSURE
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

---

#### EXPOSURE_MODE_MANUAL_EXPOSURE

public static final int EXPOSURE_MODE_MANUAL_EXPOSURE

A value to be used with the "ExposureMode" tag.

EXPOSURE_MODE_AUTO_BRACKET

```java
public static final int EXPOSURE_MODE_AUTO_BRACKET
```

A value to be used with the "ExposureMode" tag.

**See Also:** TAG_EXPOSURE_MODE

,

Constant Field Values

---

#### EXPOSURE_MODE_AUTO_BRACKET

public static final int EXPOSURE_MODE_AUTO_BRACKET

A value to be used with the "ExposureMode" tag.

TAG_WHITE_BALANCE

```java
public static final int TAG_WHITE_BALANCE
```

A tag indicating the white balance mode set when the image was shot.

**See Also:** Constant Field Values

---

#### TAG_WHITE_BALANCE

public static final int TAG_WHITE_BALANCE

A tag indicating the white balance mode set when the image was shot.

WHITE_BALANCE_AUTO

```java
public static final int WHITE_BALANCE_AUTO
```

A value to be used with the "WhiteBalance" tag.

**See Also:** TAG_WHITE_BALANCE

,

Constant Field Values

---

#### WHITE_BALANCE_AUTO

public static final int WHITE_BALANCE_AUTO

A value to be used with the "WhiteBalance" tag.

WHITE_BALANCE_MANUAL

```java
public static final int WHITE_BALANCE_MANUAL
```

A value to be used with the "WhiteBalance" tag.

**See Also:** TAG_WHITE_BALANCE

,

Constant Field Values

---

#### WHITE_BALANCE_MANUAL

public static final int WHITE_BALANCE_MANUAL

A value to be used with the "WhiteBalance" tag.

TAG_DIGITAL_ZOOM_RATIO

```java
public static final int TAG_DIGITAL_ZOOM_RATIO
```

A tag indicating the digital zoom ratio when the image was shot.

**See Also:** Constant Field Values

---

#### TAG_DIGITAL_ZOOM_RATIO

public static final int TAG_DIGITAL_ZOOM_RATIO

A tag indicating the digital zoom ratio when the image was shot.

TAG_FOCAL_LENGTH_IN_35MM_FILM

```java
public static final int TAG_FOCAL_LENGTH_IN_35MM_FILM
```

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

**See Also:** Constant Field Values

---

#### TAG_FOCAL_LENGTH_IN_35MM_FILM

public static final int TAG_FOCAL_LENGTH_IN_35MM_FILM

A tag indicating the equivalent focal length assuming a 35mm film
camera, in millimeters.

TAG_SCENE_CAPTURE_TYPE

```java
public static final int TAG_SCENE_CAPTURE_TYPE
```

A tag indicating the type of scene that was shot.

**See Also:** Constant Field Values

---

#### TAG_SCENE_CAPTURE_TYPE

public static final int TAG_SCENE_CAPTURE_TYPE

A tag indicating the type of scene that was shot.

SCENE_CAPTURE_TYPE_STANDARD

```java
public static final int SCENE_CAPTURE_TYPE_STANDARD
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### SCENE_CAPTURE_TYPE_STANDARD

public static final int SCENE_CAPTURE_TYPE_STANDARD

A value to be used with the "SceneCaptureType" tag.

SCENE_CAPTURE_TYPE_LANDSCAPE

```java
public static final int SCENE_CAPTURE_TYPE_LANDSCAPE
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### SCENE_CAPTURE_TYPE_LANDSCAPE

public static final int SCENE_CAPTURE_TYPE_LANDSCAPE

A value to be used with the "SceneCaptureType" tag.

SCENE_CAPTURE_TYPE_PORTRAIT

```java
public static final int SCENE_CAPTURE_TYPE_PORTRAIT
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### SCENE_CAPTURE_TYPE_PORTRAIT

public static final int SCENE_CAPTURE_TYPE_PORTRAIT

A value to be used with the "SceneCaptureType" tag.

SCENE_CAPTURE_TYPE_NIGHT_SCENE

```java
public static final int SCENE_CAPTURE_TYPE_NIGHT_SCENE
```

A value to be used with the "SceneCaptureType" tag.

**See Also:** TAG_SCENE_CAPTURE_TYPE

,

Constant Field Values

---

#### SCENE_CAPTURE_TYPE_NIGHT_SCENE

public static final int SCENE_CAPTURE_TYPE_NIGHT_SCENE

A value to be used with the "SceneCaptureType" tag.

TAG_GAIN_CONTROL

```java
public static final int TAG_GAIN_CONTROL
```

A tag indicating the degree of overall image gain adjustment.

**See Also:** Constant Field Values

---

#### TAG_GAIN_CONTROL

public static final int TAG_GAIN_CONTROL

A tag indicating the degree of overall image gain adjustment.

GAIN_CONTROL_NONE

```java
public static final int GAIN_CONTROL_NONE
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

---

#### GAIN_CONTROL_NONE

public static final int GAIN_CONTROL_NONE

A value to be used with the "GainControl" tag.

GAIN_CONTROL_LOW_GAIN_UP

```java
public static final int GAIN_CONTROL_LOW_GAIN_UP
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

---

#### GAIN_CONTROL_LOW_GAIN_UP

public static final int GAIN_CONTROL_LOW_GAIN_UP

A value to be used with the "GainControl" tag.

GAIN_CONTROL_HIGH_GAIN_UP

```java
public static final int GAIN_CONTROL_HIGH_GAIN_UP
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

---

#### GAIN_CONTROL_HIGH_GAIN_UP

public static final int GAIN_CONTROL_HIGH_GAIN_UP

A value to be used with the "GainControl" tag.

GAIN_CONTROL_LOW_GAIN_DOWN

```java
public static final int GAIN_CONTROL_LOW_GAIN_DOWN
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

---

#### GAIN_CONTROL_LOW_GAIN_DOWN

public static final int GAIN_CONTROL_LOW_GAIN_DOWN

A value to be used with the "GainControl" tag.

GAIN_CONTROL_HIGH_GAIN_DOWN

```java
public static final int GAIN_CONTROL_HIGH_GAIN_DOWN
```

A value to be used with the "GainControl" tag.

**See Also:** TAG_GAIN_CONTROL

,

Constant Field Values

---

#### GAIN_CONTROL_HIGH_GAIN_DOWN

public static final int GAIN_CONTROL_HIGH_GAIN_DOWN

A value to be used with the "GainControl" tag.

TAG_CONTRAST

```java
public static final int TAG_CONTRAST
```

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

**See Also:** Constant Field Values

---

#### TAG_CONTRAST

public static final int TAG_CONTRAST

A tag indicating the direction of contrast processing applied
by the camera when the image was shot.

CONTRAST_NORMAL

```java
public static final int CONTRAST_NORMAL
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

---

#### CONTRAST_NORMAL

public static final int CONTRAST_NORMAL

A value to be used with the "Contrast" tag.

CONTRAST_SOFT

```java
public static final int CONTRAST_SOFT
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

---

#### CONTRAST_SOFT

public static final int CONTRAST_SOFT

A value to be used with the "Contrast" tag.

CONTRAST_HARD

```java
public static final int CONTRAST_HARD
```

A value to be used with the "Contrast" tag.

**See Also:** TAG_CONTRAST

,

Constant Field Values

---

#### CONTRAST_HARD

public static final int CONTRAST_HARD

A value to be used with the "Contrast" tag.

TAG_SATURATION

```java
public static final int TAG_SATURATION
```

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

**See Also:** Constant Field Values

---

#### TAG_SATURATION

public static final int TAG_SATURATION

A tag indicating the direction of saturation processing
applied by the camera when the image was shot.

SATURATION_NORMAL

```java
public static final int SATURATION_NORMAL
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

---

#### SATURATION_NORMAL

public static final int SATURATION_NORMAL

A value to be used with the "Saturation" tag.

SATURATION_LOW

```java
public static final int SATURATION_LOW
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

---

#### SATURATION_LOW

public static final int SATURATION_LOW

A value to be used with the "Saturation" tag.

SATURATION_HIGH

```java
public static final int SATURATION_HIGH
```

A value to be used with the "Saturation" tag.

**See Also:** TAG_SATURATION

,

Constant Field Values

---

#### SATURATION_HIGH

public static final int SATURATION_HIGH

A value to be used with the "Saturation" tag.

TAG_SHARPNESS

```java
public static final int TAG_SHARPNESS
```

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

**See Also:** Constant Field Values

---

#### TAG_SHARPNESS

public static final int TAG_SHARPNESS

A tag indicating the direction of sharpness processing
applied by the camera when the image was shot.

SHARPNESS_NORMAL

```java
public static final int SHARPNESS_NORMAL
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

---

#### SHARPNESS_NORMAL

public static final int SHARPNESS_NORMAL

A value to be used with the "Sharpness" tag.

SHARPNESS_SOFT

```java
public static final int SHARPNESS_SOFT
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

---

#### SHARPNESS_SOFT

public static final int SHARPNESS_SOFT

A value to be used with the "Sharpness" tag.

SHARPNESS_HARD

```java
public static final int SHARPNESS_HARD
```

A value to be used with the "Sharpness" tag.

**See Also:** TAG_SHARPNESS

,

Constant Field Values

---

#### SHARPNESS_HARD

public static final int SHARPNESS_HARD

A value to be used with the "Sharpness" tag.

TAG_DEVICE_SETTING_DESCRIPTION

```java
public static final int TAG_DEVICE_SETTING_DESCRIPTION
```

A tag indicating information on the picture-taking conditions
of a particular camera model.

**See Also:** Constant Field Values

---

#### TAG_DEVICE_SETTING_DESCRIPTION

public static final int TAG_DEVICE_SETTING_DESCRIPTION

A tag indicating information on the picture-taking conditions
of a particular camera model.

TAG_SUBJECT_DISTANCE_RANGE

```java
public static final int TAG_SUBJECT_DISTANCE_RANGE
```

A tag indicating the distance to the subject.

**See Also:** Constant Field Values

---

#### TAG_SUBJECT_DISTANCE_RANGE

public static final int TAG_SUBJECT_DISTANCE_RANGE

A tag indicating the distance to the subject.

SUBJECT_DISTANCE_RANGE_UNKNOWN

```java
public static final int SUBJECT_DISTANCE_RANGE_UNKNOWN
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### SUBJECT_DISTANCE_RANGE_UNKNOWN

public static final int SUBJECT_DISTANCE_RANGE_UNKNOWN

A value to be used with the "SubjectDistanceRange" tag.

SUBJECT_DISTANCE_RANGE_MACRO

```java
public static final int SUBJECT_DISTANCE_RANGE_MACRO
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### SUBJECT_DISTANCE_RANGE_MACRO

public static final int SUBJECT_DISTANCE_RANGE_MACRO

A value to be used with the "SubjectDistanceRange" tag.

SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

```java
public static final int SUBJECT_DISTANCE_RANGE_CLOSE_VIEW
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

public static final int SUBJECT_DISTANCE_RANGE_CLOSE_VIEW

A value to be used with the "SubjectDistanceRange" tag.

SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

```java
public static final int SUBJECT_DISTANCE_RANGE_DISTANT_VIEW
```

A value to be used with the "SubjectDistanceRange" tag.

**See Also:** TAG_SUBJECT_DISTANCE_RANGE

,

Constant Field Values

---

#### SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

public static final int SUBJECT_DISTANCE_RANGE_DISTANT_VIEW

A value to be used with the "SubjectDistanceRange" tag.

TAG_IMAGE_UNIQUE_ID

```java
public static final int TAG_IMAGE_UNIQUE_ID
```

A tag indicating an identifier assigned uniquely to each image.

**See Also:** Constant Field Values

---

#### TAG_IMAGE_UNIQUE_ID

public static final int TAG_IMAGE_UNIQUE_ID

A tag indicating an identifier assigned uniquely to each image.

Method Detail

- getInstance

```java
public static
ExifTIFFTagSet
getInstance()
```

Returns a shared instance of an

ExifTIFFTagSet

.

**Returns:** an

ExifTIFFTagSet

instance.

---

#### Method Detail

getInstance

```java
public static
ExifTIFFTagSet
getInstance()
```

Returns a shared instance of an

ExifTIFFTagSet

.

**Returns:** an

ExifTIFFTagSet

instance.

---

#### getInstance

public static

ExifTIFFTagSet

getInstance()

Returns a shared instance of an

ExifTIFFTagSet

.

---

