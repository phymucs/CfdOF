#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2015 - Qingfeng Xia <qingfeng.xia()eng.ox.ac.uk>        *
#*   Copyright (c) 2017 - Johan Heyns (CSIR) <jheyns@csir.co.za>           *
#*   Copyright (c) 2017 - Oliver Oxtoby (CSIR) <ooxtoby@csir.co.za>        *
#*   Copyright (c) 2017 - Alfred Bogaers (CSIR) <abogaers@csir.co.za>      *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

__title__ = "Classes for New CFD solver"
__author__ = "Qingfeng Xia"
__url__ = "http://www.freecadweb.org"

import os.path

# NOTE: Code depreciated 25/01/2017 (JAH)
# supported_physical_domains = ['Fluidic']
# Currently the solver only support fluid analysis
# supported_physical_domains = ['Mechanical', 'Fluidic', 'Electromagnetic']  # to identify physical domains

# NOTE: Code depreciated 07/01/2017 (JAH)
# from FoamCaseBuilder import supported_turbulence_models
# from FoamCaseBuilder import supported_multiphase_models
# supported_multiphase_models = ['singplePhase']
# NOTE: Code depreciated 25/01/2017 (JAH)
# from FoamCaseBuilder import supported_radiation_models

# NOTE: Code depreciated 20/01/2017 (AB)
# Removed properties that used to reside within cfdSolver object which is either not active or
# has been relocated. Only active functionality that can be tested are included.

class CfdSolver(object):
    """ Solver specific properties. """
    def __init__(self, obj):
        self.Type = "CfdSolver"
        self.Object = obj  # keep a ref to the DocObj for nonGui usage
        obj.Proxy = self  # link between App::DocumentObject to  this object

        if "SolverName" not in obj.PropertiesList:
            obj.addProperty("App::PropertyString", "SolverName", "Solver",
                            "Name to identify the solver.", True)  # Currently not active
            obj.SolverName = "OpenFOAM"
            #obj.addProperty("App::PropertyEnumeration", "PhysicalDomain", "Solver",
                            #"unique solver name to identify the solver")
            #obj.PhysicalDomain = supported_physical_domains
            #obj.PhysicalDomain = 'Fluidic'
            #obj.addProperty("App::PropertyString", "Module", "Solver",
            #                "python module for case writer")
            obj.addProperty("App::PropertyPath", "WorkingDir", "Solver",
                            "Directory where the case is saved.")
            obj.addProperty("App::PropertyString", "InputCaseName", "Solver",
                            "Name of case containing the input files and from where the solver is executed.")
            obj.addProperty("App::PropertyBool", "Parallel", "Solver",
                            "Parallel analysis on on multiple CPU cores")
            obj.addProperty("App::PropertyInteger", "ParallelCores", "Solver",
                            "Number of cores on which to run parallel analysis")
            # obj.addProperty("App::PropertyBool", "ResultObtained", "Solver",
            #                 "Check if the results have been obtained.", True)  # Currently not active

            import tempfile
            if os.path.exists('/tmp/'):
                obj.WorkingDir = '/tmp/'  # must exist for POSIX system
            elif tempfile.tempdir:
                obj.WorkingDir = tempfile.tempdir
            else:
                obj.WorkingDir = './'
            obj.InputCaseName = 'case'

            obj.addProperty("App::PropertyFloat", "EndTime", "TimeStepControl",
                            "Duration limit if the solver did not reach convergence.")
            obj.addProperty("App::PropertyFloat", "TimeStep", "TimeStepControl",
                            "Time step increment.")
            obj.addProperty("App::PropertyFloat", "WriteInterval", "TimeStepControl",
                            "Output interval.")
            obj.addProperty("App::PropertyFloat", "ConvergenceCriteria", "TimeStepControl",
                            "Global solution convergence criterion.")

            # Default time step values
            # Temporarily use steady state (simpleFoam) compliant values
            obj.EndTime = 1000
            obj.TimeStep = 1
            obj.WriteInterval = 100
            obj.ConvergenceCriteria = 1e-4

        # NOTE: Code depreciated 06/02/2017 (JH)
        # ## API: addProperty(self,type,name='',group='',doc='',attr=0,readonly=False,hidden=False)
        # if "TurbulenceModel" not in obj.PropertiesList:

            # NOTE: Code depreciated 20/01/2017 (AB)
            # obj.addProperty("App::PropertyEnumeration", "TurbulenceModel", "CFD",
            #                 "Laminar,KE,KW,LES,etc",True)
            # obj.TurbulenceModel = list(supported_turbulence_models)
            # obj.TurbulenceModel = "laminar"
            # obj.addProperty("App::PropertyEnumeration", "MultiPhaseModel", "CFD",
            #                 "Mixing, VoF, DiscreteParticleModel")
            # obj.MultiPhaseModel = list(supported_multiphase_models)
            # DynanicMeshing, MultiPhaseModel, Combustion will not be implemented for model setup complexity
            # obj.addProperty("App::PropertyBool", "DynamicMeshing", "CFD",
            #                 "mobile/moving meshing function", True)
            # obj.addProperty("App::PropertyBool", "Compressible", "CFD",
            #                 "Compressible air or Incompressible like liquid, including temperature field", True)
            # obj.addProperty("App::PropertyBool", "transonic", "CFD",
            #                 "to support supersonic compressible flow which has specail boundary condition", True)
            # obj.addProperty("App::PropertyBool", "Porous", "CFD",
            #                 "Porous material model enabled or not", True)
            # obj.addProperty("App::PropertyBool", "NonNewtonian", "CFD",
            #                 "fluid property, strain-rate and stress constition, water and air are Newtonion", True)
            # obj.addProperty("App::PropertyVector", "Gravity", "CFD",
            #                 "gravity and other body accel")
            # obj.addProperty("App::PropertyBool", "Buoyant", "HeatTransfer",
            #                 "gravity induced flow, needed by compressible heat transfering analysis")
            # heat transfer group, conjudate and radition is not activated yet
            # obj.addProperty("App::PropertyBool", "HeatTransfering", "HeatTransfer",
            #                 "calc temperature field, needed by compressible flow")
            # obj.addProperty("App::PropertyEnumeration", "RadiationModel", "HeatTransfer",
            #                 "radiation heat transfer model", True)
            # obj.RadiationModel = list(supported_radiation_models)
            # obj.addProperty("App::PropertyBool", "Conjugate", "HeatTransfer",
            #                 "MultiRegion fluid and solid conjugate heat transfering analysis", True)

            # Transient solver related: CurrentTime TimeStep StartTime, StopTime, not activated yet!

            # NOTE: Removed the True option from addProperty to allow values be modified in the
            # GUI data tab. Current implementation does not prevent user entering negative values
            # and should be fixed once a proper settings .ui has been created.

            # obj.addProperty("App::PropertyBool", "Transient", "Transient",
            #                 "Static or transient analysis", True)
            # NOTE: This implementation does not support restart and therefor StartTime
            #       should always be set to zero.
            # obj.addProperty("App::PropertyFloat", "StartTime", "TimeStepControl",
            #                 "Time settings for transient analysis")


    def execute(self, obj):
        return

    def onChanged(self, obj, prop):
        return

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state
