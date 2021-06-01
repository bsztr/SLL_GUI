# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['MainGUI.py'],
             pathex=['C:\\Users\\Ben\\OneDrive - Mrs\\Unik_GUI'],
             binaries=[],
             datas=[("UKL.ico","."), ("tcl86t.dll","."), ("tk86t.dll","."), ("dict",".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('UnikLogo.png','C:\\Users\\Ben\\OneDrive - Mrs\\Unik_GUI\\UnikLogo.png', 'DATA')]
a.datas += [('DLLs\\Thorlabs.APT.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.APT.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.DeviceManager.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.DeviceManager.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.DeviceManagerCLI.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.DeviceManagerCLI.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.KCube.InertialMotor.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.KCube.InertialMotor.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.KCube.InertialMotorCLI.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.KCube.InertialMotorCLI.dll', 'DATA')]

a.datas += [('DLLs\\Thorlabs.MotionControl.PrivateInternal.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.PrivateInternal.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.Tools.Common.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.Tools.Common.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.Tools.Logging.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.Tools.Logging.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.Tools.WPF.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.Tools.WPF.dll', 'DATA')]
a.datas += [('DLLs\\Thorlabs.MotionControl.Tools.WPF.UI.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Thorlabs.MotionControl.Tools.WPF.UI.dll', 'DATA')]
a.datas += [('DLLs\\Xceed.Wpf.Toolkit.dll','C:\\Users\Ben\\OneDrive - Mrs\\Unik_GUI\\DLLs\\Xceed.Wpf.Toolkit.dll', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='UniKLasers',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='UKL.ico')
