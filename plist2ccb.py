import plistlib
import re
import os
import os.path
import json
import shutil
import sys
def convert():
	if len(sys.argv) < 2:
		print "./plist2ccb plist ccb"
	else:
		plist_template = plistlib.readPlistFromString(plist_template_data)
		particle_properties = plist_template.nodeGraph['properties']
		particlefile = sys.argv[1]
		ccbfile = particlefile
		if len(sys.argv) > 2:
			ccbfile = sys.argv[2]
		else:
			portion = os.path.splitext(particlefile)
			if len(portion) > 1:
				ccbfile = portion[0] + '.ccb'
			else:
				print 'input file error'
				return
		particle_dic = plistlib.readPlist(particlefile)
		p = particle_dic
		life = 1
		totalParticles = 50
		for x in range(0,len(particle_properties)):
			cprop = particle_properties[x]
			if cprop.name == 'totalParticles':
				cprop.value = particle_dic.maxParticles
				totalParticles = particle_dic.maxParticles
			elif cprop.name == 'emitterMode':
				cprop.value = particle_dic.emitterType
			elif cprop.name == 'posVar':
				cprop.value = [particle_dic.sourcePositionVariancex,particle_dic.sourcePositionVariancey]
			elif cprop.name == 'duration':
				cprop.value = p.duration
			elif cprop.name == 'life':
				cprop.value = [p.particleLifespan,p.particleLifespanVariance]
				life = p.particleLifespan
			elif cprop.name == 'startSize':
				cprop.value = [p.startParticleSize,p.startParticleSizeVariance]
			elif cprop.name == 'endSize':
				cprop.value = [p.finishParticleSize,p.finishParticleSizeVariance]
			elif cprop.name == 'startSpin':
				cprop.value = [p.rotationStart,p.rotationStartVariance]
			elif cprop.name == 'endSpin':
				cprop.value = [p.rotationEnd,p.rotationEndVariance]
			elif cprop.name == 'angle':
				cprop.value = [p.angle,p.angleVariance]
			elif cprop.name == 'startColor':
				cprop.value = [[p.startColorRed,p.startColorGreen,p.startColorBlue,p.startColorAlpha],[p.startColorVarianceRed,p.startColorVarianceGreen,p.startColorVarianceBlue,p.startColorVarianceAlpha]]
			elif cprop.name == 'endColor':
				cprop.value = [[p.finishColorRed,p.finishColorGreen,p.finishColorBlue,p.finishColorAlpha],[p.finishColorVarianceRed,p.finishColorVarianceGreen,p.finishColorVarianceBlue,p.finishColorVarianceAlpha]]
			elif cprop.name == 'blendFunc':
				cprop.value = [p.blendFuncSource,p.blendFuncDestination]
			elif cprop.name == "gravity":
				cprop.value = [p.gravityx,p.gravityy]
			elif cprop.name == "speed":
				cprop.value = [p.speed,p.speedVariance]			
			elif cprop.name == "tangentialAccel":
				cprop.value = [p.tangentialAcceleration,p.tangentialAccelVariance]
			elif cprop.name == "radialAccel":
				cprop.value = [p.radialAcceleration,p.radialAccelVariance]
			elif cprop.name == 'texture':
				cprop.value = "particle_efxpng/"+ p.textureFileName
			elif cprop.name == 'startRadius':
				cprop.value = [p.maxRadius,p.maxRadiusVariance]
			elif cprop.name == 'endRadius':
				cprop.value = [p.minRadius,0]
			elif cprop.name == 'rotatePerSecond':
				cprop.value = [p.rotatePerSecond,p.rotatePerSecondVariance]

		for x in range(0,len(particle_properties)):
			cprop = particle_properties[x]
			if cprop.name == 'emissionRate':
				if life == 0:
					cprop.value = totalParticles/0.0001
				else:
					cprop.value = totalParticles/life
		plistlib.writePlist(plist_template,ccbfile)

plist_template_data = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>centeredOrigin</key>
	<false/>
	<key>currentResolution</key>
	<integer>0</integer>
	<key>currentSequenceId</key>
	<integer>0</integer>
	<key>fileType</key>
	<string>CocosBuilder</string>
	<key>fileVersion</key>
	<integer>4</integer>
	<key>guides</key>
	<array/>
	<key>jsControlled</key>
	<false/>
	<key>nodeGraph</key>
	<dict>
		<key>baseClass</key>
		<string>CCParticleSystemQuad</string>
		<key>children</key>
		<array/>
		<key>customClass</key>
		<string></string>
		<key>displayName</key>
		<string>CCParticleSystemQuad</string>
		<key>memberVarAssignmentName</key>
		<string></string>
		<key>memberVarAssignmentType</key>
		<integer>0</integer>
		<key>properties</key>
		<array>
			<dict>
				<key>name</key>
				<string>anchorPoint</string>
				<key>type</key>
				<string>Point</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>scale</string>
				<key>type</key>
				<string>ScaleLock</string>
				<key>value</key>
				<array>
					<real>1</real>
					<real>1</real>
					<false/>
					<integer>0</integer>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>ignoreAnchorPointForPosition</string>
				<key>type</key>
				<string>Check</string>
				<key>value</key>
				<false/>
			</dict>
			<dict>
				<key>name</key>
				<string>emitterMode</string>
				<key>type</key>
				<string>IntegerLabeled</string>
				<key>value</key>
				<integer>0</integer>
			</dict>
			<dict>
				<key>name</key>
				<string>positionType</string>
				<key>type</key>
				<string>IntegerLabeled</string>
				<key>value</key>
				<integer>0</integer>
			</dict>
			<dict>
				<key>name</key>
				<string>posVar</string>
				<key>type</key>
				<string>Point</string>
				<key>value</key>
				<array>
					<real>40</real>
					<real>20</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>emissionRate</string>
				<key>type</key>
				<string>Float</string>
				<key>value</key>
				<real>80</real>
			</dict>
			<dict>
				<key>name</key>
				<string>duration</string>
				<key>type</key>
				<string>Float</string>
				<key>value</key>
				<real>-1</real>
			</dict>
			<dict>
				<key>name</key>
				<string>totalParticles</string>
				<key>type</key>
				<string>Integer</string>
				<key>value</key>
				<integer>250</integer>
			</dict>
			<dict>
				<key>name</key>
				<string>life</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>3</real>
					<real>0.25</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>startSize</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>54</real>
					<real>10</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>endSize</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>startSpin</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>endSpin</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>angle</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>90</real>
					<real>10</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>startColor</string>
				<key>type</key>
				<string>Color4FVar</string>
				<key>value</key>
				<array>
					<array>
						<real>0.75999999046325684</real>
						<real>0.25</real>
						<real>0.11999999731779099</real>
						<real>255</real>
					</array>
					<array>
						<real>0.0</real>
						<real>0.0</real>
						<real>0.0</real>
						<real>0.0</real>
					</array>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>endColor</string>
				<key>type</key>
				<string>Color4FVar</string>
				<key>value</key>
				<array>
					<array>
						<real>0.0</real>
						<real>0.0</real>
						<real>0.0</real>
						<real>255</real>
					</array>
					<array>
						<real>0.0</real>
						<real>0.0</real>
						<real>0.0</real>
						<real>0.0</real>
					</array>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>blendFunc</string>
				<key>type</key>
				<string>Blendmode</string>
				<key>value</key>
				<array>
					<integer>1</integer>
					<integer>1</integer>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>startRadius</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>endRadius</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>rotatePerSecond</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>60</real>
					<real>20</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>gravity</string>
				<key>type</key>
				<string>Point</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>speed</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>60</real>
					<real>20</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>tangentialAccel</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>radialAccel</string>
				<key>type</key>
				<string>FloatVar</string>
				<key>value</key>
				<array>
					<real>0.0</real>
					<real>0.0</real>
				</array>
			</dict>
			<dict>
				<key>name</key>
				<string>texture</string>
				<key>type</key>
				<string>Texture</string>
				<key>value</key>
				<string>pve_cloud/cloud01.png</string>
			</dict>
		</array>
		<key>selected</key>
		<true/>
	</dict>
	<key>notes</key>
	<array/>
	<key>resolutions</key>
	<array>
		<dict>
			<key>centeredOrigin</key>
			<false/>
			<key>ext</key>
			<string>iphone</string>
			<key>height</key>
			<integer>0</integer>
			<key>name</key>
			<string>iPhone</string>
			<key>scale</key>
			<real>1</real>
			<key>width</key>
			<integer>0</integer>
		</dict>
	</array>
	<key>sequences</key>
	<array>
		<dict>
			<key>autoPlay</key>
			<true/>
			<key>callbackChannel</key>
			<dict>
				<key>keyframes</key>
				<array/>
				<key>type</key>
				<integer>10</integer>
			</dict>
			<key>chainedSequenceId</key>
			<integer>-1</integer>
			<key>length</key>
			<real>10</real>
			<key>name</key>
			<string>Default Timeline</string>
			<key>offset</key>
			<real>0.0</real>
			<key>position</key>
			<real>0.0</real>
			<key>resolution</key>
			<real>30</real>
			<key>scale</key>
			<real>128</real>
			<key>sequenceId</key>
			<integer>0</integer>
			<key>soundChannel</key>
			<dict>
				<key>keyframes</key>
				<array/>
				<key>type</key>
				<integer>9</integer>
			</dict>
		</dict>
	</array>
	<key>stageBorder</key>
	<integer>3</integer>
</dict>
</plist>
'''

'''
{
"angleVariance"
"duration"
"blendFuncSource"
"blendFuncDestination"
"startColorRed"
"startColorGreen"
"startColorBlue"
"startColorAlpha"
"startColorVarianceRed"
"startColorVarianceGreen"
"startColorVarianceBlue"
"startColorVarianceAlpha"
"finishColorRed"
"finishColorGreen"
"finishColorBlue"
"finishColorAlpha"
"finishColorVarianceRed"
"finishColorVarianceGreen"
"finishColorVarianceBlue"
"finishColorVarianceAlpha"
"startParticleSize"
"startParticleSizeVariance"
"finishParticleSize"
"finishParticleSizeVariance"
"sourcePositionx"
"sourcePositiony"
"sourcePositionVariancex"
"sourcePositionVariancey"
"rotationStart"
"rotationStartVariance"
"rotationEnd"
"rotationEndVariance"
"emitterType"
"gravityx"
"gravityy"
"speed"
"speedVariance"
"radialAcceleration"
"radialAccelVariance"
"tangentialAcceleration"
"tangentialAccelVariance"
"rotationIsDir"
"maxRadius"
"maxRadiusVariance"
"minRadius"
"rotatePerSecond"
"rotatePerSecondVariance"
"particleLifespan"
"particleLifespanVariance"
"textureFileName"
}
'''
convert()
